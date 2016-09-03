#!/usr/bin/env python
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from math import floor

DEBUG = False
STRICT = True

fontName = 'STSong-Light'

def init():
    pdfmetrics.registerFont(UnicodeCIDFont(fontName))


def auto_adapt(ux, uy, text):
    fs = floor(uy / 0.6)
    print('fs:', fs)
    while stringWidth(text, fontName, fs)/0.8 >= ux:
        fs -= 1
        print('fs:', fs)
    px = stringWidth(text, fontName, fs)
    print('px:', px)
    py = fs * 0.6
    print('py:', py)
    return fs, px, py

def generate(filePath, width, height, line, column, text):
    ux = width/column
    uy = height/line

    fontSize, px, py = auto_adapt(ux, uy, text)

    dx = (ux-px)/2
    dy = (uy-py)/2

    c = Canvas(filePath, pagesize=(width, height))
    c.setFont(fontName, fontSize)
    if DEBUG:
        c.lines(get_lines(width, height, line, column))
    for i in range(0, column):
        for j in range(0, line):
            c.drawString(i*ux+dx, j*uy+dy, text)
    c.save()
    return build_return(0, 'Success!')


def get_lines(width, height, line, column):
    ux = width/column
    uy = height/line
    lines = []
    lines.extend([(i*ux, 0, i*ux, height) for i in range(0, column+1)])
    lines.extend([(0, i*uy, width, i*uy) for i in range(0, line+1)])
    return lines


def build_return(code, msg):
    return {'code': code, 'msg': msg}

if __name__ == '__main__':
    DEBUG = True
    fp = 'test.pdf'
    w = 12.2
    h = 20.8
    l = 15
    c = 5
    text = 'Hello 世界!'
    init()
    generate(fp, w*cm, h*cm, l, c, text)
