from flask import Flask, render_template, request, redirect, url_for
import os
from os.path import join, dirname, realpath
from .db import DB

app = Flask(__name__)
app.config["DEBUG"] = True

UPLOAD_FOLDER = 'files/'
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def index():
    return render_template('index.html')

def safe_dir(dir_name: os.PathLike) -> None:
    if os.path.exists(dir_name):
        return
    else:
        os.mkdir(dir_name)
        return

@app.route("/", methods=['POST'])
def upload_files():

    duckdb = DB()
    safe_dir(app.config['UPLOAD_FOLDER'])
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
        uploaded_file.save(file_path)
    return duckdb.query_file(file_path)
    # return redirect(url_for('index'))

if (__name__=="__main__"):
    app.run(port=5000)