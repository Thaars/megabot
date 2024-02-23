import json
import os
import zlib

import definitions
import local_config
import strategy
import dataframe
import plot
import indicator
import test_configs
from api import get_all_binance, get_stock_data, get_tradovate_data
from db import DB
from portfolio import Portfolio
from definitions import *
import pandas as pd
import pandas_ta as ta

import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error
from keras.models import Sequential, load_model
from keras.layers import Dense, LSTM, Dropout
from keras.callbacks import EarlyStopping
import numpy as np
import mplfinance as mpf
from sklearn.impute import KNNImputer
from datetime import date, datetime
from test_configs import *
from local_config import *

'''
# laufend den GPU Speicher im CLI anzeigen- - refresh jede Sekunde
nvidia-smi -l 1
'''


def main():
    if local_config.FORCE_USE_CPU:
        os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

    if local_config.FORCE_USE_TEST_CONFIGS:
        for config in test_configs:
            execute(config)
    else:
        execute(local_config.SINGLE_CONFIG)


def execute(config):
    # # todo: remove test data
    # # Konfiguration
    # steps = [1, 2, 3, 5, 10]
    # num_samples = 100  # Stellen Sie sicher, dass dies größer ist als sequence_length + max(steps)
    # start_value = 100
    # step_increase = 1
    #
    # # Simulieren von original_data mit Volatilität
    # np.random.seed(42)  # Für reproduzierbare Ergebnisse
    # volatility = 2  # Einstellen der Volatilität der simulierten Preisbewegungen
    # close_values_volatility = [100 + i + np.random.randn() * volatility for i in range(num_samples + max(steps))]
    # original_data = pd.DataFrame({'close': close_values_volatility})
    #
    # # Simulieren von predictions mit einer ähnlichen Volatilität wie original_data
    # predictions = {
    #     step: np.array([100 + i + np.random.randn() * volatility for i in range(num_samples)]) for step in steps
    # }
    #
    # directional_accuracy = evaluate_directional_accuracy(predictions, steps, original_data, config['sequence_length'])
    # print(f"{directional_accuracy}")
    # # todo: remove test data

    ai_model_path = 'ai_models/'
    prediction_candles = [1, 2, 3, 5, 10, 15]

    print('-----------------------------------------------------------')
    print(json.dumps(config))

    db = DB()
    # prepare_df_for_training
    df, scaler, x_train, y_train, x_test, y_test, train_start_time, train_end_time, test_start_time, test_end_time, \
        num_features, feature_columns, df_train, df_test = prepare_df_for_training(config, prediction_candles)

    # suchen des models in der db anhand von model_hash
    model_hash = create_hash(config, train_start_time, train_end_time)
    ai_model_filename = f'{ai_model_path}{model_hash}.keras'
    model_from_db = db.get_model_from_db(model_hash)

    print(f"\tmodel_hash: {model_hash}")
    print('-----------------------------------------------------------')

    if os.path.isfile(ai_model_filename) and not model_from_db:
        print(f"Model found at file system, but missing in DB - saving model to DB")
        db.save_model_to_db(config, train_start_time, train_end_time, model_hash)

    if model_from_db and os.path.isfile(ai_model_filename):
        print(f"Model found at file system and in DB - load existing model")
        model = load_model(ai_model_filename)
    else:
        print(f"Model not found - train new model")
        model = train_model(db, config, num_features, x_train, y_train, x_test, y_test, feature_columns,
                            ai_model_filename, model_from_db, train_start_time, train_end_time, model_hash,
                            len(prediction_candles))

    print('-----------------------------------------------------------')

    # Verwende diese Funktion, um die Vorhersagen für jeden Schritt zu generieren
    predictions = generate_predictions_for_all_steps(model, x_test, prediction_candles)

    # Finden des Indexes des Features "close"
    close_index = feature_columns.index('close')
    # Initialisiere ein neues Dictionary für die rückskalierten Vorhersagen
    predictions_rescaled = {}
    for step, preds in predictions.items():
        # Erstellen eines Dummy-Arrays mit der erwarteten Form
        # Hier nehmen wir an, dass der Scaler ursprünglich auf Daten mit einer Länge von 'len(feature_columns)'
        # Features angepasst wurde
        dummy_array = np.zeros((preds.shape[0], len(feature_columns)))
        # Setzen Sie die Vorhersagen in die Spalte, die dem 'close'-Feature entspricht
        # Da preds bereits ein 1D-Array ist, ordnen wir diese Werte direkt der entsprechenden Spalte zu
        dummy_array[:, close_index] = preds
        # Rückskalieren des gesamten Dummy-Arrays
        # Dieses Mal geben wir das gesamte Dummy-Array an den Scaler, was den Erwartungen des Scalers entspricht
        predictions_rescaled_array = scaler.inverse_transform(dummy_array)
        # Extrahieren der rückskalierten Vorhersagen für das 'close'-Feature
        # Und speichern der rückskalierten Vorhersagen für diesen Schritt im Dictionary
        predictions_rescaled[step] = predictions_rescaled_array[:, close_index]

    directional_accuracy = evaluate_directional_accuracy(predictions_rescaled, prediction_candles, df,
                                                         config['sequence_length'])
    print(f"{directional_accuracy}")


    # todo
    # Anomalien identifizieren
    # anomalies = detect_anomalies(long_term_predictions, window_size=5, threshold=2.0)  # Beispielwerte


    # predict_directions
    # directions, predicted_prices_steps, actual_prices = predict_directions(df, model, x_test, num_features,
    #                                                                        scaler, [1, 2, 3, 5, 10, 15])
    # predicted_directions, predicted_prices, actual_prices = predict_directions(df, model, x_test, num_features, scaler)

    # # Langzeitvorhersagen machen
    # long_term_predictions = make_long_term_predictions(model, x_test, 10)
    #
    # # Rücktransformation der Vorhersagen
    # # Hinweis: Dies setzt voraus, dass Sie bereits einen Scaler definiert und angepasst haben
    # dummy_data = np.zeros((long_term_predictions.shape[0] * long_term_predictions.shape[1], num_features))
    # dummy_data[:, 3] = long_term_predictions.flatten()  # Angenommen, der Preis ist das letzte Feature
    # actual_data = scaler.inverse_transform(dummy_data)
    # actual_prices = actual_data[:, 3].reshape(long_term_predictions.shape[0], long_term_predictions.shape[1])
    #
    # # Mittelwert der tatsächlichen Preise berechnen
    # long_term_predictions_mean = np.mean(actual_prices, axis=0).squeeze()
    #
    # # Die folgenden Schritte bleiben unverändert
    # mse = mean_squared_error(y_test, long_term_predictions_mean)
    # mae = mean_absolute_error(y_test, long_term_predictions_mean)
    # long_term_average_price = df['close'].mean()  # Durchschnittspreis von Bitcoin
    # mae_percent = (mae / long_term_average_price) * 100
    # mse_percent = (np.sqrt(mse) / long_term_average_price) * 100
    # current_price = df['close'].iloc[-1]  # Letzter bekannter Preis
    # predicted_price = long_term_predictions_mean[-1]  # Vorhergesagter Preis am Ende des Vorhersagezeitraums
    # percent_change = ((predicted_price - current_price) / current_price) * 100
    #
    # print(f"MAE als Prozentsatz des Durchschnittspreises: {round(mae_percent, 4)}%")
    # print(f"RMSE als Prozentsatz des Durchschnittspreises: {round(mse_percent, 4)}%")
    # print(f"Durchschnittliche prozentuale Veränderung: {round(percent_change, 4)}%")
    #
    # # actual_changes = calculate_price_changes(y_test)
    # # predicted_changes = calculate_price_changes(long_term_predictions.squeeze())
    # # total_correct, percentage_correct, accuracy_up, accuracy_down = calculate_direction_accuracy_and_percentage(
    # #     actual_changes, predicted_changes)
    # #
    # # print(f"TREND: Gesamtzahl der korrekten Vorhersagen: {total_correct}")
    # # print(f"TREND: Prozentualer Anteil der korrekten Vorhersagen: {round(percentage_correct, 4)}%")
    # # print(f"TREND: Genauigkeit bei steigenden Kursen: {round(accuracy_up, 4)}%")
    # # print(f"TREND: Genauigkeit bei fallenden Kursen: {round(accuracy_down, 4)}%")
    #
    # predicted_overall_trend = calculate_overall_trend(long_term_predictions.squeeze())
    # actual_overall_trend = calculate_overall_trend(y_test)
    # # Vergleichen der Trends
    # correct_trend_prediction = predicted_overall_trend == actual_overall_trend
    # # Berechnen der Genauigkeit
    # accuracy = np.mean(correct_trend_prediction) * 100  # In Prozent umrechnen
    # print(f"Genauigkeit der Gesamttrendvorhersage: {round(accuracy, 4)}%")
    # # Berechne die Genauigkeit für steigende und fallende Kurse
    # # Stellen Sie sicher, dass y_test und long_term_predictions korrekt vorbereitet sind
    # accuracy_up, accuracy_down = calculate_trend_accuracy(long_term_predictions.squeeze(), y_test)
    # print(f"Genauigkeit bei steigenden Kursen: {accuracy_up}%")
    # print(f"Genauigkeit bei fallenden Kursen: {accuracy_down}%")
    # # # Ergebnisse ausgeben, wenn anwendbar
    # # if accuracy_up is not None:
    # #     print(f"Genauigkeit bei steigenden Kursen: {accuracy_up * 100}%")
    # # else:
    # #     print("Keine steigenden Kurse im Testzeitraum.")
    # # if accuracy_down is not None:
    # #     print(f"Genauigkeit bei fallenden Kursen: {accuracy_down * 100}%")
    # # else:
    # #     print("Keine fallenden Kurse im Testzeitraum.")
    #
    # # plot_chart
    # plot_chart(df, predicted_directions)
    #
    # # Berechnung der Preisänderungen
    # actual_changes = np.diff(actual_prices)
    # predicted_changes = np.diff(predicted_prices)
    # total_correct, percentage_correct, accuracy_up, accuracy_down = calculate_direction_accuracy_and_percentage(
    #     actual_changes, predicted_changes
    # )
    #
    # print(f"NEXT CANDLE: Anzahl aller Vorhersagen: {len(predicted_prices)}")
    # print(f"NEXT CANDLE: Gesamtzahl der korrekten Vorhersagen: {round(total_correct, 4)}")
    # print(f"NEXT CANDLE: Prozentualer Anteil der korrekten Vorhersagen: {round(percentage_correct, 4)} %")
    # print(f"NEXT CANDLE: Genauigkeit bei steigenden Kursen: {round(accuracy_up, 4)} %")
    # print(f"NEXT CANDLE: Genauigkeit bei fallenden Kursen: {round(accuracy_down, 4)} %")
    #
    # # todo: SPEICHERN **************************************************************************************************
    # # todo: SPEICHERN **************************************************************************************************
    # # todo: SPEICHERN **************************************************************************************************
    # # db.save_predictions_to_db(config, test_start_time, test_end_time, model_hash, len(predicted_prices), total_correct,
    # #                           percentage_correct, accuracy_up, accuracy_down, mse_percent, mae_percent)
    # # todo: SPEICHERN **************************************************************************************************
    # # todo: SPEICHERN **************************************************************************************************
    # # todo: SPEICHERN **************************************************************************************************

    return


def create_sequences_with_multiple_targets(df, scaled_data, sequence_length, steps, close_column_position):
    x, y = [], []
    for i in range(len(scaled_data) - sequence_length - max(steps)):
        x_seq = scaled_data[i:(i + sequence_length)]
        x.append(x_seq)

        # Extrahiert den skalierten "Close"-Wert für jeden der definierten zukünftigen Schritte
        y_seq = [scaled_data[i + sequence_length + step - 1, close_column_position] for step in steps]
        y.append(y_seq)

    return np.array(x), np.array(y)


def evaluate_directional_accuracy(predictions, prediction_candles, df, sequence_length):
    results = {}
    for step in prediction_candles:
        accuracy_buckets = {f"{i * 10}% - {i * 10 + 10}%": 0 for i in range(10)}
        correct_predictions = 0
        total_predictions = 0

        # Stellen Sie sicher, dass die Schleife innerhalb des Bereichs von predictions[step] bleibt
        # Die Anzahl der Iterationen sollte die kleinere der beiden Größen sein: len(predictions[step]) oder len(df) - step - sequence_length
        max_iterations = min(len(predictions[step]), len(df) - step - sequence_length)

        for i in range(max_iterations):
            pred_value = predictions[step][i]
            actual_index = i + sequence_length + step
            # Überprüfen, ob der tatsächliche Index innerhalb der Grenzen von df liegt
            if actual_index < len(df):
                actual_value = df.iloc[actual_index]['close']

                # Berechnung des absoluten prozentualen Fehlers (APE)
                ape = abs(pred_value - actual_value) / actual_value * 100 if actual_value != 0 else 0

                # Bestimmung des entsprechenden Genauigkeitsbereichs
                bucket_index = int(ape // 10)
                bucket_index = min(bucket_index, 9)  # Maximaler Index ist 9 für den Bereich 90% - 100%
                bucket_key = f"{bucket_index * 10}% - {bucket_index * 10 + 10}%"
                accuracy_buckets[bucket_key] += 1

                total_predictions += 1

        results[step] = {
            "Anzahl korrekter Vorhersagen": f"{correct_predictions} von {total_predictions} "
                                            f"(entspricht {(correct_predictions / total_predictions * 100):.2f}%)",
            "Genauigkeitsbereiche": accuracy_buckets
        }

    return results


# def evaluate_directional_accuracy(predictions, steps, original_data, sequence_length):
#     results = {}
#     for step in steps:
#         correct_direction_count = 0
#         direction_accuracy_buckets = {f"{i * 10}% - {i * 10 + 10}%": {'steigend': 0, 'fallend': 0} for i in range(10)}
#
#         # Extrahiere die tatsächlichen Werte für den aktuellen Schritt
#         actuals = original_data.shift(-step)['close'].values[sequence_length:-step]
#
#         for i in range(len(predictions[step])):
#             pred_change = predictions[step][i] - original_data.iloc[i + sequence_length - 1]['close']
#             actual_change = actuals[i] - original_data.iloc[i + sequence_length - 1]['close']
#
#             # Überprüfe, ob die Vorhersage die korrekte Richtung hat
#             if np.sign(pred_change) == np.sign(actual_change):
#                 correct_direction_count += 1
#                 percent_error = abs(pred_change - actual_change) / abs(actual_change) * 100
#
#                 # Bestimme den Genauigkeitsbucket
#                 bucket_index = int(percent_error // 10)
#                 bucket_index = min(bucket_index, 9)  # Begrenze auf den höchsten Bucket
#
#                 direction = 'steigend' if pred_change > 0 else 'fallend'
#                 direction_accuracy_buckets[f"{bucket_index * 10}% - {bucket_index * 10 + 10}%"][direction] += 1
#
#         total_predictions = len(predictions[step])
#         results[step] = {
#             "Anzahl korrekter Richtungsvorhersagen": f"{correct_direction_count} von {total_predictions} (entspricht "
#                                                      f"{(correct_direction_count / total_predictions * 100):.2f}%)",
#             "Genauigkeitsbereiche": direction_accuracy_buckets
#         }
#
#     return results


# def create_sequences(df, scaled_data, sequence_length):
#     close_column_index = df.columns.get_loc("close")
#     x = []
#     y = []
#     for i in range(len(scaled_data) - sequence_length):
#         sequence = scaled_data[i:(i + sequence_length)]
#         label = scaled_data[i + sequence_length, close_column_index]  # Nehmen wir an, dass 'Close' die Zielvariable ist
#         x.append(sequence)
#         y.append(label)
#     return np.array(x), np.array(y)


# Funktion zur Berechnung der Genauigkeit basierend auf Bewegungsrichtung
def calculate_accuracy_for_direction(actual_changes, predicted_changes, direction_mask):
    direction_actual_changes = actual_changes[direction_mask]
    direction_predicted_changes = predicted_changes[direction_mask]

    # Berechnung des prozentualen Fehlers
    actual_abs_changes = np.abs(direction_actual_changes)
    predicted_abs_changes = np.abs(direction_predicted_changes)
    percentage_error = np.abs(predicted_abs_changes - actual_abs_changes) / actual_abs_changes

    # Klassifizierung der Genauigkeit
    accuracy_25 = np.sum(percentage_error <= 0.25)
    accuracy_50 = np.sum(percentage_error <= 0.50)
    accuracy_75 = np.sum(percentage_error <= 0.75)

    return accuracy_25, accuracy_50, accuracy_75


def calculate_overall_trend(prices):
    # Vergleichen des ersten und letzten Preises, um den Gesamttrend zu bestimmen
    return np.sign(prices[-1] - prices[0])


def calculate_direction_accuracy_and_percentage(actual_changes, predicted_changes):
    # Bestimmen der tatsächlichen und vorhergesagten Richtung
    actual_directions = np.sign(actual_changes)
    predicted_directions = np.sign(predicted_changes)

    # Bestimmen, wann Vorhersage und tatsächliche Richtung übereinstimmen
    correct_predictions = actual_directions == predicted_directions

    # Berechnen der Gesamtanzahl der korrekten Vorhersagen
    total_correct = np.sum(correct_predictions)

    # Berechnen der Gesamtanzahl der Vorhersagen
    total_predictions = len(predicted_changes)  # oder actual_changes, da beide gleich lang sein sollten

    # Bestimmen der korrekten Vorhersagen für steigende und fallende Kurse
    correct_up = np.sum(correct_predictions & (actual_directions == 1))
    correct_down = np.sum(correct_predictions & (actual_directions == -1))

    # Berechnen der Genauigkeit für steigende und fallende Kurse
    accuracy_up = correct_up / total_predictions * 100  # In Prozent
    accuracy_down = correct_down / total_predictions * 100  # In Prozent

    # Berechnen des prozentualen Anteils der korrekten Vorhersagen an allen Vorhersagen
    percentage_correct = total_correct / total_predictions * 100  # In Prozent

    return total_correct, percentage_correct, accuracy_up, accuracy_down


def create_hash(config, start_time, end_time):
    general_hash_values = [
        json.dumps(config),
        f'{start_time}',
        f'{end_time}',
    ]
    return zlib.adler32(json.dumps(general_hash_values).encode('UTF-8')) & 0xffffffff


def prepare_df_for_training(config, prediction_candles):
    filename = get_all_binance(config['symbol'], config['timeframe'])
    df = dataframe.trading_data_from_csv(filename)

    df = indicator.last_5_10_15_20_candles(df, filename)
    df = indicator.last_30_40_50_75_100_candles(df, filename)
    df = indicator.aroon(df, filename, definitions.AROON_PERIOD)
    df = indicator.ma_cross(df, filename, definitions.MA_FAST_PERIOD, definitions.MA_SLOW_PERIOD)
    df = indicator.fractals(df, filename, definitions.FRACTALS_PERIOD)
    df = indicator.parabolic_sar(df, filename, definitions.PARABOLIC_SAR_ACCELERATION_FACTOR,
                                 definitions.PARABOLIC_SAR_MAX_ACCELERATION_FACTOR)
    df = indicator.volume_sma(df, filename, definitions.VOLUME_SMA_PERIOD)
    df = indicator.williams_r(df, filename, definitions.WILLIAMS_R_PERIOD)
    df = indicator.vortex_indicator(df, filename, definitions.VORTEX_INDICATOR_PERIOD)
    df = indicator.ema(df, filename, definitions.EMA_PERIOD)
    df = indicator.accumulation_distribution(df, filename)
    df = indicator.chaikin_volatility(df, filename, definitions.CHAIKIN_VOLATILITY_EMA_PERIOD,
                                      definitions.CHAIKIN_VOLATILITY_CHANGE_PERIOD)
    df = indicator.macd(df, filename, definitions.MACD_SHORT_PERIOD, definitions.MACD_LONG_PERIOD,
                        definitions.MACD_SIGNAL_PERIOD)
    df = indicator.historical_volatility(df, filename, definitions.HISTORICAL_VOLATILITY_PERIOD)
    df = indicator.rsi(df, filename, definitions.RSI_PERIOD)
    df = indicator.bollinger_bands(df, filename, definitions.BOLLINGER_BANDS_PERIOD,
                                   definitions.BOLLINGER_BANDS_NUM_STD)
    df = indicator.ichimoku_cloud(df, filename)
    df = indicator.hma(df, filename, definitions.HMA_PERIOD)
    df = indicator.elders_force_index(df, filename, definitions.ELDERS_FORCE_INDEX_PERIOD)
    df = indicator.demarker_indicator(df, filename, definitions.DEMARKER_INDICATOR_PERIOD)
    df = indicator.fibonacci_retracements(df, filename, definitions.FIBONACCI_RETRACEMENTS_PERIOD)
    df = indicator.keltner_channels(df, filename, definitions.KELTNER_CHANNELS_EMA_PERIOD,
                                    definitions.KELTNER_CHANNELS_ATR_PERIOD, definitions.KELTNER_CHANNELS_MULTIPLIER)
    df = indicator.average_true_range(df, filename, definitions.AVERAGE_TRUE_RANGE_PERIOD)

    df = df.loc[f'{definitions.START_DATE}':f'{definitions.END_DATE}']

    # # Ursprüngliche Anzahl der Zeilen
    # original_row_count = len(df)
    # # Schritt 1A: Frühesten gültigen Zeitpunkt für jede Spalte bestimmen
    # first_valid_timestamps = df.apply(lambda col: col.first_valid_index())
    # # Schritt 2A: Spätesten dieser frühesten Zeitpunkte ermitteln
    # latest_first_valid_timestamp = first_valid_timestamps.max()
    # # Schritt 1B: Letzten gültigen Zeitpunkt für jede Spalte bestimmen
    # last_valid_timestamps = df.apply(lambda col: col.last_valid_index())
    # # Schritt 2B: Frühesten dieser letzten Zeitpunkte ermitteln
    # earliest_last_valid_timestamp = last_valid_timestamps.min()
    # # Schritt 3: DataFrame filtern, um nur Daten zwischen diesen Zeitpunkten einzuschließen
    # filtered_df = df.loc[latest_first_valid_timestamp:earliest_last_valid_timestamp]
    # # Anzahl der entfernten Zeilen am Anfang und Ende berechnen
    # rows_removed_start = df.index.get_loc(latest_first_valid_timestamp)
    # rows_removed_end = original_row_count - df.index.get_loc(earliest_last_valid_timestamp) - 1
    # # Verbliebene Zeilen
    # remaining_rows = len(filtered_df)
    # # Ausgabe der Ergebnisse
    # print(f"Entfernte Zeilen am Anfang: {rows_removed_start}")
    # print(f"Entfernte Zeilen am Ende: {rows_removed_end}")
    # print(f"Verbliebene Zeilen: {remaining_rows}")
    # df = filtered_df

    # Liste von Spaltennamen, die als Features dienen sollen
    feature_columns = config['columns']
    # Anzahl der Features dynamisch aus der Länge der feature_columns Liste ableiten
    num_features = len(feature_columns)

    split_index = int(len(df) * config['split_index'])  # z.B. 80% der Daten für das Training
    df_train = df[:split_index]
    df_test = df[split_index:]

    # Start- und Endzeitpunkt der Trainingsdaten
    train_start_time = df_train.index[0]
    train_end_time = df_train.index[-1]
    # Start- und Endzeitpunkt der Testdaten
    test_start_time = df_test.index[0]
    test_end_time = df_test.index[-1]

    # Auswahl der Feature-Spalten für Trainings- und Testdatensätze
    df_train_features = df_train[feature_columns]
    df_test_features = df_test[feature_columns]

    # fehlende Werte interpolieren
    imputer = KNNImputer(n_neighbors=5)
    df_train_features = pd.DataFrame(imputer.fit_transform(df_train_features), columns=df_train_features.columns)
    df_test_features = pd.DataFrame(imputer.fit_transform(df_test_features), columns=df_test_features.columns)
    # df_train_features.interpolate(method='polynomial', inplace=True)
    # df_test_features.interpolate(method='polynomial', inplace=True)

    # Skalieren der Feature-Daten
    scaler = MinMaxScaler()
    scaled_train_data = scaler.fit_transform(df_train_features)  # Skalieren basierend auf Trainingsdaten
    scaled_test_data = scaler.transform(df_test_features)  # Anwendung derselben Transformation auf Testdaten

    # Anzahl der Datenpunkte für die Sequenz (wird benutzt um den nachfolgenden Datenpunkt vorherzusagen)
    sequence_length = config['sequence_length']
    # Berechne die Position der Close-Spalte basierend auf den Feature-Columns
    close_column_position = feature_columns.index('close')
    # Umformen der Daten für das LSTM-Modell
    x_train, y_train = create_sequences_with_multiple_targets(df_train, scaled_train_data, sequence_length,
                                                              prediction_candles, close_column_position)
    x_test, y_test = create_sequences_with_multiple_targets(df_test, scaled_test_data, sequence_length,
                                                            prediction_candles, close_column_position)

    return df, scaler, x_train, y_train, x_test, y_test, train_start_time, train_end_time, test_start_time, \
           test_end_time, num_features, feature_columns, df_train, df_test


def train_model(db, config, num_features, x_train, y_train, x_test, y_test, feature_columns, ai_model_filename,
                model_from_db, train_start_time, train_end_time, model_hash, output_steps):
    print(f"start training")
    model = Sequential()
    for layer in range(config['layers']):
        model.add(LSTM(units=config['neurones'], return_sequences=True,
                       input_shape=(config['sequence_length'], num_features), kernel_initializer='glorot_uniform'))
        model.add(Dropout(0.5))  # Dropout-Schicht mit 50% Auslasswahrscheinlichkeit
    model.add(LSTM(units=config['neurones'], kernel_initializer='glorot_uniform'))
    model.add(Dropout(0.5))  # Dropout-Schicht mit 50% Auslasswahrscheinlichkeit
    model.add(Dense(output_steps, kernel_initializer='he_normal'))

    # EarlyStopping Callback definieren
    early_stopper = EarlyStopping(
        monitor='val_loss',  # Überwachung des Validierungsverlustes
        min_delta=0.0001,  # Die minimale Veränderung, die als Verbesserung betrachtet wird
        patience=10,  # Anzahl der Epochen ohne signifikante Verbesserung
        verbose=1,  # Ausgabe von Meldungen aktivieren
        mode='min',  # Der Modus 'min' bedeutet, dass das Training bei einer Abnahme des 'val_loss' gestoppt wird
        restore_best_weights=True  # Setzt die Modellgewichte auf die aus der besten Epoche zurück
    )

    # Kompilieren des Modells
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Trainieren des Modells
    model.fit(
        x=x_train,
        y=y_train,
        batch_size=config['batch_size'],
        epochs=config['epochs'],
        validation_data=(x_test, y_test),
        callbacks=[early_stopper]  # EarlyStopping-Callback hinzufügen
    )

    # Überprüfen, ob Early Stopping stattgefunden hat
    if early_stopper.stopped_epoch > 0:
        early_stopping_epoch = early_stopper.stopped_epoch
    else:
        early_stopping_epoch = None

    # Bestimmen der Größe der Stichprobe
    sample_size = 100  # zum Beispiel 1000
    # Wählen einer zufälligen Stichprobe aus x_train
    indices = np.random.choice(x_train.shape[0], sample_size, replace=False)
    x_train_sample = x_train[indices]

    # evaluate_model ist eine Funktion, die Ihr Modell mit einem Datensatz bewertet
    # und eine Leistungsmetrik zurückgibt (z.B. Genauigkeit, MSE, etc.)
    baseline_performance = evaluate_model(model, x_test, y_test)
    feature_importances = []
    for i in range(x_test.shape[2]):  # Iterieren über Feature-Dimension
        x_test_permuted = x_test.copy()
        np.random.shuffle(x_test_permuted[:, :, i])  # Permutieren nur dieses Features
        permuted_performance = evaluate_model(model, x_test_permuted, y_test)
        importance = baseline_performance - permuted_performance  # Leistungsunterschied
        feature_importances.append(importance)
    # Konvertieren in absolute Werte
    absolute_importances = np.abs(feature_importances)
    # Normalisieren der absoluten Werte auf eine Skala von 0 bis 100
    normalized_importances = (absolute_importances / np.sum(absolute_importances)) * 100
    # Zuordnung der normalisierten Importanzen zu den Feature-Namen
    importances_with_names = list(zip(feature_columns, normalized_importances))
    # Sortieren der Features basierend auf ihrer normalisierten Wichtigkeit
    sorted_importances = sorted(importances_with_names, key=lambda x: x[1], reverse=True)
    # Ausgabe der sortierten, normalisierten Feature-Importanzen
    for name, importance in sorted_importances:
        print(f"{name}: {importance:.2f}%")

    # todo: SPEICHERN **************************************************************************************************
    # todo: SPEICHERN **************************************************************************************************
    # todo: SPEICHERN **************************************************************************************************
    # # Speichern
    # model.save(ai_model_filename)
    # # in die DB nur, wenn es n noch keinen Eintrag gibt
    # # das kann passieren, wenn es bereits ein Model und den DB eintrag gab, das model dann aber gelöscht wurde
    # if not model_from_db:
    #     db.save_model_to_db(config, train_start_time, train_end_time, model_hash, early_stopping_epoch,
    #                         json.dumps(feature_importances))
    # todo: SPEICHERN **************************************************************************************************
    # todo: SPEICHERN **************************************************************************************************
    # todo: SPEICHERN **************************************************************************************************

    print(f"training completed")

    return model


def generate_predictions_for_all_steps(model, x_test, prediction_candles):
    # Generiere Vorhersagen für den gesamten Testdatensatz
    predictions = model.predict(x_test)

    # Initialisiere ein Dictionary, um die Vorhersagen für die verschiedenen Schritte zu speichern
    step_predictions = {candle: [] for candle in prediction_candles}

    # Ordne jede Spalte in den Vorhersagen dem entsprechenden Schritt zu
    # Dies setzt voraus, dass die Ausgabe des Modells in der Reihenfolge der Schritte organisiert ist
    steps = prediction_candles
    for i, step in enumerate(steps):
        step_predictions[step] = predictions[:, i]

    return step_predictions


def predict_directions(df, model, x_test, num_features, scaler, steps):
    # Vorhersagen des Modells
    predicted_prices = model.predict(x_test)
    # Bereite das Ergebnis-Dictionary vor
    directions = {}
    predicted_prices_steps = {}

    # Durchlaufe die verschiedenen Schritte für die Vorhersage
    for step in steps:
        # Anpassung: Direkte Berechnung der Preisänderungen für zukünftige Schritte
        price_changes = []
        for i in range(len(predicted_prices) - step):
            change = predicted_prices[i + step] - predicted_prices[i]
            price_changes.append(change)
        price_changes = np.array(price_changes)

        # Bestimme die Richtungen basierend auf den Preisänderungen
        predicted_directions = np.sign(price_changes.squeeze())
        directions[f"directions_{step}_steps"] = predicted_directions

        # Keine Anpassung nötig, da die Preise direkt vorhergesagt werden
        if step == 1:
            predicted_prices_steps[f"prices_{step}_steps"] = predicted_prices.squeeze()[:-step]
        else:
            # Für Schritte größer als 1, nutze den Originalpreis, adjustiert um die Schrittzahl
            predicted_prices_steps[f"prices_{step}_steps"] = predicted_prices.squeeze()[:-step]

    # Extrahiere die tatsächlichen Preise für den Vergleich
    max_step = max(steps)
    actual_prices = df['close'].values[-(len(predicted_prices)-max_step):]

    return directions, predicted_prices_steps, actual_prices


# def predict_directions(df, model, x_test, num_features, scaler):
#     # Verwendung des Modells zur Vorhersage
#     predicted_prices = model.predict(x_test)
#     # Berechnen der Differenzen zwischen aufeinanderfolgenden vorhergesagten Preisen
#     price_changes = np.diff(predicted_prices.squeeze(), prepend=predicted_prices[0])
#     # Bestimmen der Richtungen basierend auf den Preisänderungen (1 für steigend, -1 für fallend)
#     predicted_directions = np.sign(price_changes)
#     # Umwandeln von 0 zu -1, falls Sie keine neutralen Vorhersagen haben möchten
#     predicted_directions[predicted_directions == 0] = -1
#     # Angenommen, predicted_prices ist Ihr Array von vorhergesagten 'close' Preisen mit Form (n_samples, 1)
#     # Erstellen Sie ein Dummy-Array mit Nullen oder einem anderen Platzhalterwert
#     # für die anderen Spalten, die beim Skalieren berücksichtigt wurden
#     dummy_features = np.zeros(
#         (predicted_prices.shape[0], num_features - 1))  # Erstellt ein Array von Nullen für die restlichen Features
#     # Fügen Sie die vorhergesagten Preise zu diesem Array hinzu, um die korrekte Form zu erhalten
#     predicted_full = np.concatenate([dummy_features, predicted_prices], axis=1)
#     # Wenden Sie inverse_transform auf dieses vollständige Array an
#     predicted_full_inverse = scaler.inverse_transform(predicted_full)
#     # Extrahieren Sie die skalierten 'close' Preise (angenommen, sie befinden sich in der letzten Spalte)
#     predicted_prices = predicted_full_inverse[:, -1]
#     n = len(predicted_prices)
#     actual_prices = df['close'][-n:].values
#
#     return predicted_directions, predicted_prices, actual_prices


def calculate_price_changes(prices):
    # Überprüfen, ob prices mehr als eine Dimension hat und entsprechend handeln
    if prices.ndim > 1:
        # Annahme: Wir wollen die Preisänderungen über die erste Dimension berechnen
        changes = np.diff(prices, axis=0)
    else:
        # Für eindimensionale Arrays, wie ursprünglich implementiert
        prices_with_initial = np.insert(prices, 0, prices[0])
        changes = np.diff(prices_with_initial)
    return changes


def make_long_term_predictions(model, x_train, num_predictions):
    predictions = []
    current_input = x_train
    for _ in range(num_predictions):
        # Vorhersage für den aktuellen Input
        current_prediction = model.predict(current_input)
        predictions.append(current_prediction)
        # Aktualisieren des Inputs, um die nächste Vorhersage zu machen
        current_input = np.roll(current_input, -1, axis=1)
        current_input[:, -1, :] = current_prediction
    return np.array(predictions)


def calculate_trend_accuracy(predicted_prices, actual_prices):
    # Berechnung des Gesamttrends für die vorhergesagten Preise
    predicted_trend = np.sign(predicted_prices[-1] - predicted_prices[0])
    # Berechnung des Gesamttrends für die tatsächlichen Preise
    actual_trend = np.sign(actual_prices[-1] - actual_prices[0])
    # Vergleich der Gesamttrends
    correct_prediction = int(predicted_trend == actual_trend)
    # Berechnung der Genauigkeit für steigende und fallende Trends
    accuracy_up = correct_prediction if actual_trend > 0 else None
    accuracy_down = correct_prediction if actual_trend < 0 else None

    return accuracy_up, accuracy_down


def plot_chart(df, predicted_directions):
    if local_config.PLOT_CHART:
        print("Zu vergleichende Kerzen: ", local_config.CHART_LENGTH)
        # Erstellen einer expliziten Kopie von df, um SettingWithCopyWarning zu vermeiden
        filtered_df = df.iloc[-local_config.CHART_LENGTH:].copy()
        # Schneiden Sie die predicted_directions, um nur die letzten n Richtungen zu haben
        filtered_predicted_directions = predicted_directions[-local_config.CHART_LENGTH:]
        # zum aktuellen df hinzufügen
        filtered_df.loc[:, 'Predictions'] = filtered_predicted_directions

        # Erstellen einer Serie, die `NaN` für die `close`-Preise setzt, wo die Vorhersage nicht 1 oder -1 ist
        up_prices = filtered_df['close'].where(filtered_df['Predictions'] == 1)
        down_prices = filtered_df['close'].where(filtered_df['Predictions'] == -1)
        # Erstellen der Addplot-Objekte
        up_scatter = mpf.make_addplot(up_prices, type='scatter', markersize=100, marker='^', color='green')
        down_scatter = mpf.make_addplot(down_prices, type='scatter', markersize=100, marker='v', color='red')

        # Erstellen des kombinierten Candlestick-Charts mit vorhergesagten Richtungen
        mpf.plot(filtered_df, type='candle', style='charles', addplot=[up_scatter, down_scatter],
                 volume=True, figratio=(10, 6), title='Tatsächliche Kurse mit Vorhersagen')


def detect_anomalies(predictions, window_size, threshold):
    anomalies = []
    moving_avg = pd.Series(predictions).rolling(window=window_size).mean()
    residual = abs(predictions - moving_avg)

    for i in range(len(residual)):
        if residual[i] > threshold:
            anomalies.append((i, predictions[i]))

    return anomalies


def evaluate_model(model, x_test, y_test):
    predictions = model.predict(x_test)
    mse = mean_squared_error(y_test, predictions)
    return mse


# TensorFlow-Protokollierungsebene einstellen
# 0 = alle Meldungen
# 1 = INFO-Meldungen werden gefiltert
# 2 = zusätzlich WARN-Meldungen werden gefiltert
# 3 = zusätzlich ERROR-Meldungen werden gefiltert
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

main()
