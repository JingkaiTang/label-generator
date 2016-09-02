#!/usr/bin/env python
from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.units import cm


def generate(filePath, fontName, fontSize, width, height, line, column, text):
    c = canvas.Canvas(filePath, pagesize=(width, height))
    c.setFont(fontName, fontSize, leading=1)
    c.lines(getLines(width, height, line, column))
    ux = width/column
    uy = height/line
    px = stringWidth(text, fontName, fontSize)
    py = fontSize*0.6
    dx = (ux-px)/2
    dy = (uy-py)/2
    for i in range(0, column):
        for j in range(0, line):
            c.drawString(i*ux+dx, j*uy+dy, text)
    c.save()


def getLines(width, height, line, column):
    ux = width/column
    uy = height/line
    lines = []
    lines.extend([(i*ux, 0, i*ux, height) for i in range(0, column+1)])
    lines.extend([(0, i*uy, width, i*uy) for i in range(0, line+1)])
    return lines

if __name__ == '__main__':
    fp = "test.pdf"
    fn = "Helvetica"
    fs = 15
    w = 12
    h = 12
    l = 12
    c = 4
    text = "Hello World!"
    generate(fp, fn, fs, w*cm, h*cm, l, c, text)
