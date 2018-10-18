from flask import Flask, render_template
import sqlite3

# to run:
# cd to directory
# source env/bin/activate or env/bin/activate.bat
# export FLASK_APP=run.py; export FLASK_DEBUG=1 or set FLASK_APP=run.py; set FLASK_DEBUG=1
# flask run

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
