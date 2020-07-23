#!/usr/bin/env python

import cairo
import subprocess

def intersection (line1,line2):
  """Line-Line intersection

  From: en.wikipedia.org/wiki/Line-line_intersection
  """
  ((x1,y1),(x2,y2)) = line1
  ((x3,y3),(x4,y4)) = line2
  nx = (x1*y2-y1*x2) * (x3-x4) - (x1-x2) * (x3*y4-y3*x4)
  ny = (x1*y2-y1*x2) * (y3-y4) - (y1-y2) * (x3*y4-y3*x4)
  d  = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
  parallel = (d == 0)
  if parallel:
    return None
  else:
    x  = nx / d
    y  = ny / d
    return (x,y)

w_pic, h_pic = 160,110
w,h = 150,100

filename = "armature-2.pdf"
surface = cairo.PDFSurface(filename, w_pic, h_pic)
ct = cairo.Context(surface)

ct.rectangle(0, 0, w_pic, h_pic)
ct.set_source_rgb(1.0, 1.00, 1.00)
ct.fill()

def rect (t1,t2):
  (x1,y1),(x2,y2) = t1,t2
  ct.rectangle (x1, y1, x2-x1, y2-y1)
  
def line (p1,p2):
  x1,y1 = p1
  x2,y2 = p2
  ct.move_to (x1,y1)
  ct.line_to (x2,y2)

x1,y1 = 5,5
x2,y2 = x1 + w, y1 + h

ps = [(x1,y1),(x2,y1),(x2,y2),(x1,y1)]

line (ps[0],ps[2])
rect ((x1,y1),(x2,y2))

ct.set_source_rgb(0.00, 0.00, 0.00)
ct.set_line_width(1.0)
ct.stroke()

subprocess.Popen(["mupdf " + filename],shell=True)

