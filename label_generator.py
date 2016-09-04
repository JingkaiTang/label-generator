#!/usr/bin/env python
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from math import floor

DEBUG = False
STRICT = True
X_RATIO = 0.8
Y_RATIO = 0.8

fontName = 'STSong-Light'
title = ''
subject = '不干胶标签打印'
author = 'Jingkai Tang'
creator = 'Label Generator'


def init():
    pdfmetrics.registerFont(UnicodeCIDFont(fontName))

init()


def autoFit(ux, uy, text):
    log('Auto Fitting...')
    fs = floor(uy * Y_RATIO / 0.6)
    if fs < 1:
        fs = 1
    log('font size: %s' % fs)
    while fs != 1 and stringWidth(text, fontName, fs)/X_RATIO >= ux:
        fs -= 1
        log('font size: %s' % fs)
    px = stringWidth(text, fontName, fs)
    log('px: %s' % px)
    py = fs * 0.6
    log('py: %s' % py)
    return fs, px, py

def generate(filePath, width, height, line, column, text):
    width *= cm
    height *= cm
    ux = width/column
    uy = height/line

    fontSize, px, py = autoFit(ux, uy, text)

    dx = (ux-px)/2
    dy = (uy-py)/2

    c = Canvas(filePath, pagesize=(width, height))
    c.setAuthor(author)
    c.setCreator(creator)
    c.setTitle(text)
    c.setSubject(subject)
    c.setFont(fontName, fontSize)
    if DEBUG:
        c.lines(get_lines(width, height, line, column))
    for i in range(0, column):
        for j in range(0, line):
            c.drawString(i*ux+dx, j*uy+dy, text)
    c.save()


def get_lines(width, height, line, column):
    ux = width/column
    uy = height/line
    lines = []
    lines.extend([(i*ux, 0, i*ux, height) for i in range(0, column+1)])
    lines.extend([(0, i*uy, width, i*uy) for i in range(0, line+1)])
    return lines


def log(msg):
    if DEBUG:
        print(msg)

if __name__ == '__main__':
    DEBUG = True
    fp = 'test.pdf'
    w = 12.2
    h = 20.8
    l = 15
    c = 5
    text = 'Hello 世界!'
    generate(fp, w, h, l, c, text)
