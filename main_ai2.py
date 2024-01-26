import subprocess
import json
import os

from test_configs import test_configs


use_test_configs = True


def run_subprocess_with_config(subprocess_config, use_gpu=True, attempt=1):
    config_str = json.dumps(subprocess_config)
    command = ["python", "execute_ai2.py", config_str]

    # Setzen der Umgebungsvariablen für die GPU-Nutzung
    env = dict(os.environ, CUDA_VISIBLE_DEVICES=('0' if use_gpu else '-1'))

    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True, env=env)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Fehler während der Ausführung:", e.stderr)
        if "tensorflow.python.framework.errors_impl.ResourceExhaustedError" in e.stderr:
            print("TensorFlow ResourceExhaustedError erkannt.")
            if attempt < 2:  # Verhindern einer Endlosschleife
                print("Fallback zu CPU")
                run_subprocess_with_config(subprocess_config, use_gpu=False, attempt=attempt + 1)
            else:
                print("Maximale Anzahl von Versuchen erreicht, Abbruch.")
        else:
            print("Unbekannter Fehler, Abbruch.")


if use_test_configs:
    for config in test_configs:
        run_subprocess_with_config(config)
else:
    config = {
        'symbol': 'BTCUSDT',
        'timeframe': '30m',
        'layers': 10,
        'neurones': 100,
        # Liste von Spaltennamen, die als Features dienen sollen
        'columns': ['open', 'high', 'low', 'close',
                    'aroon_25_up', 'aroon_25_down',
                    'ma_7', 'ma_26', 'ma_golden_cross_7_26', 'ma_death_cross_7_26',
                    'fractal_5_bullish', 'fractal_5_bearish'],
        # Anzahl der Datenpunkte für die Sequenz (wird benutzt um den nachfolgenden Datenpunkt vorherzusagen)
        'sequence_length': 30,
        # Berechnen des Trennindex - 80% der Daten für das Training
        'split_index': 0.8,
        'epochs': 1,
    }
    run_subprocess_with_config(config)

