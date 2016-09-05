#!/usr/bin/env python
from flask import Flask, request, jsonify, send_from_directory, redirect
from label_generator import generate as pdfG
import datetime
import os
import uuid
import json

app = Flask(__name__)
gen_dir = 'gen'
log_dir = 'log'


@app.route('/generatePDF', methods=['GET', 'POST'])
def generatePDF():
    width = request.form['width']
    width = float(width)
    height = request.form['height']
    height = float(height)
    line = request.form['line']
    line = int(line)
    column = request.form['column']
    column = int(column)
    text = request.form['text']
    log('Generate: width: %s, height: %s, line: %s, column: %s, text: %s' % (width, height, line, column, text))
    gf = randF()
    pdfG(gf, width, height, line, column, text)
    return jsonify({'pdf': gf})


@app.route('/')
def root():
    return redirect('/index.html', code=302)


@app.route('/<path:path>')
def web(path):
    return send_from_directory('web', path)


@app.route('/gen/<path:path>')
def gen(path):
    return send_from_directory('gen', path)


@app.route('/data', methods=['GET', 'POST'])
def data():
    return jsonify(json.load(open('data/specs.json')))


def randF():
    if not os.path.exists(gen_dir):
        os.mkdir(gen_dir)
    return os.path.join(gen_dir, str(uuid.uuid4())+'.pdf')


def log(msg):
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)
    now = datetime.datetime.now()
    log_f = os.path.join(log_dir, now.strftime('%Y-%m-%d.log'))
    open(log_f, 'a').write('[%s] %s\n' % (now.strftime('%H:%M:%S'), msg))

if __name__ == '__main__':
    app.run()
