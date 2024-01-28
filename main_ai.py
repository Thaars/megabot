import json
import os
import zlib

import definitions
import strategy
import dataframe
import plot
import indicator
import test_configs
from api import get_all_binance, get_stock_data, get_tradovate_data
from db import DB
from portfolio import Portfolio
from definitions import *

from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential, load_model
from keras.layers import Dense, LSTM
from keras.callbacks import EarlyStopping
import numpy as np
import mplfinance as mpf
from datetime import date, datetime
from test_configs import *

'''
# laufend den GPU Speicher im CLI anzeigen- - refresh jede Sekunde
nvidia-smi -l 1
'''


def main():
    # os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
    use_test_configs = False

    if use_test_configs:
        for config in test_configs:
            execute(config)
    else:
        config = {
            'symbol': 'BTCUSDT',
            'timeframe': '30m',
            'layers': 3,
            'neurones': 100,
            # Liste von Spaltennamen, die als Features dienen sollen
            'columns': ['open', 'high', 'low', 'close',
                        'aroon_25_up', 'aroon_25_down',
                        'ma_7', 'ma_26', 'ma_golden_cross_7_26', 'ma_death_cross_7_26',
                        'fractal_5_bullish', 'fractal_5_bearish'],
            # Anzahl der Datenpunkte für die Sequenz (wird benutzt um den nachfolgenden Datenpunkt vorherzusagen)
            'sequence_length': 30,
            # Berechnen des Trennindex - 80% der Daten für das Training
            'split_index': 0.7,
            'epochs': 50,
            # mittlere Größe als Kompromiss (32, 64, 128)
            # je größer desto mehr Speicherbedarf
            # todo: einkommentieren !!! ist auskommentiert, da auf dem Server die sdeicherung eines modells nicht
            #  möglich war - soll erkennen, dass es ein modell gibt, die config dazu speichern und testen - danach
            #  diese batch size verwenden und unten im code die config verwenden statt der harten 1 - ggf. methode
            #  um die batch size bestehenden models in der db hinzuizufügen
            #  (config anpassen, hash berechnen, db updaten, model name updaten)
            # 'batch_size': 32
        }
        execute(config)


def execute(config):
    ai_model_path = 'ai_models/'
    chart = False
    # Anzahl der Kerzen, die vom Ende des Dataframes für den Plot verwendet werden sollen
    chart_length = 500

    print(json.dumps(config))

    db = DB()
    filename = get_all_binance(config['symbol'], config['timeframe'])
    df = dataframe.trading_data_from_csv(filename)

    df = indicator.last_5_10_15_20_candles(df, filename)
    df = indicator.aroon(df, filename, definitions.AROON_PERIOD)
    df = indicator.ma_cross(df, filename, definitions.MA_FAST_PERIOD, definitions.MA_SLOW_PERIOD)
    df = indicator.fractals(df, filename, definitions.FRACTALS_PERIOD)

    df = df.loc[f'{definitions.START_DATE}':f'{definitions.END_DATE}']

    # Schritt 1: Frühesten gültigen Zeitpunkt für jede Spalte bestimmen
    first_valid_timestamps = df.apply(lambda col: col.first_valid_index())
    # Schritt 2: Spätesten dieser frühesten Zeitpunkte ermitteln
    latest_first_valid_timestamp = first_valid_timestamps.max()
    # Schritt 3: DataFrame filtern, um nur Daten ab diesem Zeitpunkt einzuschließen
    df = df.loc[latest_first_valid_timestamp:]

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

    # Skalieren der Feature-Daten
    scaler = MinMaxScaler()
    scaled_train_data = scaler.fit_transform(df_train_features)  # Skalieren basierend auf Trainingsdaten
    scaled_test_data = scaler.transform(df_test_features)  # Anwendung derselben Transformation auf Testdaten

    # Anzahl der Datenpunkte für die Sequenz (wird benutzt um den nachfolgenden Datenpunkt vorherzusagen)
    sequence_length = config['sequence_length']
    # Umformen der Daten für das LSTM-Modell
    x_train, y_train = create_sequences(df_train, scaled_train_data, sequence_length)
    x_test, y_test = create_sequences(df_test, scaled_test_data, sequence_length)

    # suchen des models in der db anhand von model_hash
    model_hash = create_hash(config, train_start_time, train_end_time)
    ai_model_filename = f'{ai_model_path}{model_hash}.keras'
    model_from_db = db.get_model_from_db(model_hash)

    if os.path.isfile(ai_model_filename) and not model_from_db:
        db.save_model_to_db(config, train_start_time, train_end_time, model_hash)

    if model_from_db and os.path.isfile(ai_model_filename):
        model = load_model(ai_model_filename)
    else:
        model = Sequential()
        for layer in range(config['layers']):
            model.add(LSTM(units=config['neurones'], return_sequences=True, input_shape=(None, num_features)))
        model.add(LSTM(units=config['neurones']))
        model.add(Dense(1))

        # EarlyStopping Callback definieren
        early_stopper = EarlyStopping(
            monitor='val_loss',  # Überwachung des Validierungsverlustes
            min_delta=0.001,  # Die minimale Veränderung, die als Verbesserung betrachtet wird
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
            batch_size=1,#config['batch_size'],
            epochs=config['epochs'],
            validation_data=(x_test, y_test),
            callbacks=[early_stopper]  # EarlyStopping-Callback hinzufügen
        )

        # Speichern
        model.save(ai_model_filename)
        # in die DB nur, wenn es n noch keinen Eintrag gibt
        # das kann passieren, wenn es bereits ein Model und den DB eintrag gab, das model dann aber gelöscht wurde
        if not model_from_db:
            db.save_model_to_db(config, train_start_time, train_end_time, model_hash)

    # Verwendung des Modells zur Vorhersage
    predicted_prices = model.predict(x_test)
    # Berechnen der Differenzen zwischen aufeinanderfolgenden vorhergesagten Preisen
    price_changes = np.diff(predicted_prices.squeeze(), prepend=predicted_prices[0])
    # Bestimmen der Richtungen basierend auf den Preisänderungen (1 für steigend, -1 für fallend)
    predicted_directions = np.sign(price_changes)
    # Umwandeln von 0 zu -1, falls Sie keine neutralen Vorhersagen haben möchten
    predicted_directions[predicted_directions == 0] = -1
    # Angenommen, predicted_prices ist Ihr Array von vorhergesagten 'close' Preisen mit Form (n_samples, 1)
    # Erstellen Sie ein Dummy-Array mit Nullen oder einem anderen Platzhalterwert
    # für die anderen Spalten, die beim Skalieren berücksichtigt wurden
    dummy_features = np.zeros(
        (predicted_prices.shape[0], num_features-1))  # Erstellt ein Array von Nullen für die restlichen Features
    # Fügen Sie die vorhergesagten Preise zu diesem Array hinzu, um die korrekte Form zu erhalten
    predicted_full = np.concatenate([dummy_features, predicted_prices], axis=1)
    # Wenden Sie inverse_transform auf dieses vollständige Array an
    predicted_full_inverse = scaler.inverse_transform(predicted_full)
    # Extrahieren Sie die skalierten 'close' Preise (angenommen, sie befinden sich in der letzten Spalte)
    predicted_prices = predicted_full_inverse[:, -1]
    n = len(predicted_prices)
    actual_prices = df['close'][-n:].values

    if chart:
        print("Zu vergleichende Kerzen: ", chart_length)
        # Erstellen einer expliziten Kopie von df, um SettingWithCopyWarning zu vermeiden
        filtered_df = df.iloc[-chart_length:].copy()
        # Schneiden Sie die predicted_directions, um nur die letzten n Richtungen zu haben
        filtered_predicted_directions = predicted_directions[-chart_length:]
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

    # Berechnung der Preisänderungen
    actual_changes = np.diff(actual_prices)
    predicted_changes = np.diff(predicted_prices)
    total_correct, percentage_correct, accuracy_up, accuracy_down = calculate_direction_accuracy_and_percentage(
        actual_changes, predicted_changes
    )

    print(f"Anzahl aller Vorhersagen: {len(predicted_prices)}")
    print(f"Gesamtzahl der korrekten Vorhersagen: {total_correct}")
    print(f"Prozentualer Anteil der korrekten Vorhersagen: {percentage_correct} %")
    print(f"Genauigkeit bei steigenden Kursen: {accuracy_up} %")
    print(f"Genauigkeit bei fallenden Kursen: {accuracy_down} %")

    db.save_predictions_to_db(config, test_start_time, test_end_time, model_hash, len(predicted_prices), total_correct,
                              percentage_correct, accuracy_up, accuracy_down)

    return


def create_sequences(df, scaled_data, sequence_length):
    close_column_index = df.columns.get_loc("close")
    x = []
    y = []
    for i in range(len(scaled_data) - sequence_length):
        sequence = scaled_data[i:(i + sequence_length)]
        label = scaled_data[i + sequence_length, close_column_index]  # Nehmen wir an, dass 'Close' die Zielvariable ist
        x.append(sequence)
        y.append(label)
    return np.array(x), np.array(y)


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













main()
