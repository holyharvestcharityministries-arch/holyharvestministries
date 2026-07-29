from flask import Flask, render_template

import threading
import requests
import time 

from pathlib import Path

dev_marker_file = Path("./_local_dev_env")
DEV_ENV = False

if dev_marker_file.exists():
    print("DEV ENV!")
    DEV_ENV = True


app = Flask(__name__)

def keep_alive():
    # Wait for the server to start
    time.sleep(10)
    # Replace with your actual Render URL
    url = "https://holyharvest.onrender.com/health"

    while True:
        try:
            requests.get(url)
            print("Self-ping successful.")
        except Exception as e:
            print(f"Self-ping failed: {e}")

        # Ping every 14 minutes (Render sleeps after 15)
        time.sleep(14 * 60)
        # time.sleep(10)

if not DEV_ENV:
    threading.Thread(target=keep_alive, daemon=True).start()


@app.route('/health')
def health():
    return "OK", 200

@app.route("/")
def index():
    return render_template("index.html", title="Holy Harvest Charity Ministries")
