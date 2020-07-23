#!/usr/bin/env python

import cairo
import math
import subprocess

class Point:
  def __init__ (self, x=0, y=0):
    self.x = x
    self.y = y
  def __repr__ (self):
    return f"Point ({self.x},{self.y})"
  def __add__(self, p2):
    return Point (self.x + p2.x, self.y + p2.y)
  def pair (self):
    return (self.x,self.y)

class Line: 
  def __init__ (self, p1, p2):
    self.p1 = p1
    self.p2 = p2
  def __repr__ (self):
    return (f"Line ({self.p1.x},{self.p1.y}) "
            f"-- ({self.p2.x},{self.p2.y})")

class Polygon:
  def __init__ (self, ps):
    self.ps = ps


def clip (subjectPolygon, clipPolygon):
  """ Sutherland-Hodgman polygon clipping

  rosettacode.org/wiki/Sutherland-Hodgman_polygon_clipping
  en.wikipedia.org/wiki/Sutherland%E2%80%93Hodgman_algorithm
  """
  def inside (p):
    return (
     cp2[0]-cp1[0])*(p[1]-cp1[1]) > (cp2[1]-cp1[1])*(p[0]-cp1[0])
 
  def computeIntersection ():
    dc = [ cp1[0] - cp2[0], cp1[1] - cp2[1] ]
    dp = [ s[0] - e[0], s[1] - e[1] ]
    n1 = cp1[0] * cp2[1] - cp1[1] * cp2[0]
    n2 = s[0] * e[1] - s[1] * e[0] 
    n3 = 1.0 / (dc[0] * dp[1] - dc[1] * dp[0])
    return [
      (n1*dp[0] - n2*dc[0]) * n3, (n1*dp[1] - n2*dc[1]) * n3 ]
 
  outputList = subjectPolygon
  cp1 = clipPolygon [-1]
 
  for clipVertex in clipPolygon:
    cp2 = clipVertex
    inputList = outputList
    outputList = []
    s = inputList [-1]
 
    for subjectVertex in inputList:
      e = subjectVertex
      if inside (e):
        if not inside (s):
          outputList.append(computeIntersection())
        outputList.append(e)
      elif inside (s):
        outputList.append(computeIntersection())
      s = e
    cp1 = cp2
  return (outputList)

def intersection (line1,line2):
  """Line-Line intersection

  From: en.wikipedia.org/wiki/Line-line_intersection
  """
  p1,p2 = line1.p1,line1.p2
  p3,p4 = line2.p1,line2.p2
  (x1,y1),(x2,y2) = (p1.x,p1.y),(p2.x,p2.y)
  (x3,y3),(x4,y4) = (p3.x,p3.y),(p4.x,p4.y)
  nx = (x1*y2-y1*x2) * (x3-x4) - (x1-x2) * (x3*y4-y3*x4)
  ny = (x1*y2-y1*x2) * (y3-y4) - (y1-y2) * (x3*y4-y3*x4)
  d  = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
  parallel = (d == 0)
  if parallel:
    return None
  else:
    x  = nx / d
    y  = ny / d
    return Point (x,y)

w_pic, h_pic = 160,110
w,h = 150,100

filename = "armature-5.pdf"
surface = cairo.PDFSurface (filename, w_pic, h_pic)
ct = cairo.Context (surface)

ct.rectangle (0, 0, w_pic, h_pic)
ct.set_source_rgb (1.0, 1.00, 1.00)
ct.fill()

def draw_point (pt):
  ct.arc (pt.x,pt.y,3,0,math.tau)
  ct.set_source_rgb (0, 0, 0)
  ct.fill ()

def draw_rect (p1,p2):
  ct.rectangle (p1.x, p1.y, p2.x - p1.x, p2.y - p1.y)
  
def draw_line (line):
  p1,p2 = line.p1,line.p2
  ct.move_to (p1.x,p1.y)
  ct.line_to (p2.x,p2.y)

def draw_polygon (ps):
  ct.move_to (ps[0].x,ps[0].y)
  for t in ps[1:]:
    ct.line_to (t.x,t.y)
  ct.close_path ()
  ct.set_source_rgb (1, 0.5, 0)
  ct.fill ()

def center (a,b):
  return Point ((a.x + b.x) / 2, (a.y + b.y) / 2)

def pairs (pt):
  return (pt.x, pt.y)

x1,y1 = 5,5
x2,y2 = x1 + w, y1 + h

ps = [Point (x1,y1),Point (x2,y1),Point (x2,y2),Point (x1,y2)]
# pg1 = Polygon ps
# hs = [Point (x1,y1),Point (x2,y1),Point (x1,y2)]
# pts3 = clip ([p.pair () for p in ps],[p.pair () for p in hs]) 
# pg3 = [Point (x,y) for [x,y] in pts3]
# print (ps)
# draw_polygon (pg3)

# draw_rect (ps[0],ps[2])

ct.set_source_rgb (0.00, 0.00, 0.00)
ct.set_line_width (1.0)
ct.stroke ()

# diagonal1 = Line (ps[0],ps[2])
# diagonal2 = Line (ps[1],ps[3])

# draw_line (diagonal1)
# draw_line (diagonal2)
# ct.stroke ()

# print (diagonal1)
# print (diagonal2)
# center1 = intersection (diagonal1,diagonal2)
cs = [center (ps[i],ps[(i+1)%len(ps)]) for i,e in enumerate (ps)]
ts = []
for (a,b) in zip (ps,cs):
  ts.extend ([a,b])
cutd = [(0,2),(2,4),(4,6),(0,6)]
print (ts)
t = range (len (ts))
s1 = {(a,b) for a in t for b in t if a < b if (a,b) not in cutd}
ks = [Line (ts[a],ts[b]) for (a,b) in s1]

# print (cs)
for k in ks:
  draw_line (k)
ct.stroke ()

for p in ts:
  draw_point (p)


subprocess.Popen (["mupdf " + filename],shell=True)

