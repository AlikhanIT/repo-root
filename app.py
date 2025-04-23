from flask import Flask
from prometheus_client import Counter, generate_latest
import logging
from logging.handlers import RotatingFileHandler
import os

# === Инициализация Flask ===
app = Flask(__name__)

# === Инициализация логирования ===
log_dir = 'logs'
log_file = os.path.join(log_dir, 'app.log')

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

file_handler = RotatingFileHandler(log_file, maxBytes=10 * 1024, backupCount=5)
file_handler.setFormatter(logging.Formatter(
    '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
))
file_handler.setLevel(logging.INFO)

app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
app.logger.info("🚀 Flask app has started.")

# === Prometheus метрики ===
home_counter = Counter('homepage_hits_total', 'Total visits to the homepage')

# === Роуты ===
@app.route("/")
def home():
    home_counter.inc()
    app.logger.info("Home page accessed.")
    return "✅ Hello from CI/CD + Prometheus!"

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain'}

# === Запуск приложения ===
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
