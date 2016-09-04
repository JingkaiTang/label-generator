#!/usr/bin/env python
from flask import Flask, request, jsonify, send_from_directory
from label_generator import generate as pdfG
import datetime
import os

app = Flask(__name__)

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
    ret = pdfG('sstest.pdf', width, height, line, column, text)
    return jsonify(ret)


@app.route('/web')
@app.route('/web/<path:path>')
def web_static(path=None):
    if not path:
        path = 'index.html'
    return send_from_directory('web', path)


def log(msg):
    log_dir = 'log'
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)
    now = datetime.datetime.now()
    log_f = os.path.join(log_dir, now.strftime('%Y-%m-%d.log'))
    open(log_f, 'a').write('[%s] %s\n' % (now.strftime('%H:%M:%S'), msg))

if __name__ == '__main__':
    app.run()
