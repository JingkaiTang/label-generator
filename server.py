#!/usr/bin/env python
from flask import Flask, request, jsonify
from label_generator import generate as pdfG

app = Flask(__name__)

@app.route('/', methods=['POST'])
def generatePDF():
    params = request.json
    ret = pdfG('sstest.pdf', params['width'], params['height'], params['line'], params['column'], params['text'])
    return jsonify(ret)

if __name__ == '__main__':
    app.run()
