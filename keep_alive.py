# keep_alive.py
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive", 200

@app.route('/health')
def health():
    return "OK", 200

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
