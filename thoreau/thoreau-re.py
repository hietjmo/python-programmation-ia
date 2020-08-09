
# python thoreau-re.py IED-utf8.txt fi20.txt thesauro-2.txt

from tkinter import *
import sys
import time

def prt (*xs,sep=' ',end='\n'):
  x = sep.join ([str (x) for x in xs])
  text1.insert ("end", x + end)

def linea (char='-',length=60):
  prt (length * char)

# lines = ['line 1\n','line 2\n', 'line 3\n']
def read_args ():
  s1 = sys.argv[0]
  prt (s1.capitalize())
  prt (len (s1)* "=","\n")
  idx1,idx2 = "1.0", "1."+str(len (s1))
  text1.tag_add("gray", idx1, idx2)
  prt ('Dictionarios legite / argumentos del programma')
  linea ()
  lines = []
  arguments = sys.argv
  for i,e in enumerate (arguments):
    if i > 0:
      prt (f"{i}: {e}")
      filename = arguments[i]
      with open (filename) as f:
        lines = lines + f.readlines ()
  linea ()
  prt ("In toto",len (lines),"lineas")
  linea ()
  return lines

def try_compile (word):
  regex = None
  if len (word) > 0:
    try:
      regex = re.compile (word)
    except:
      pass
  return regex

def find_words (word):
  xs = []
  regex = try_compile (word)
  if regex:
    for s in lines:
      m = regex.search (s)
      if m: 
        xs.append ((m.start(),s))
    xs.sort ()
  ys = xs [:max_m]  
  result = [str (i+1) + " ▶ " + s for i,(b,s) in enumerate (ys)]
  d = len (xs) - len (ys)
  if d > 0: 
    result.append (f"(+ {d} alteres)")
  return result

def find_all (s,sub):
  start = 0
  while True:
    start = s.find (sub,start)
    if start == -1: return
    yield start
    start = start + len (sub) 

def highlight (result,word):
  regex = try_compile (word)
  for i,n in enumerate (result):
    for m in regex.finditer (n):
      a,b = m.span ()
      idx1 = f"{i+1}.{a}"
      idx2 = f"{i+1}.{b}"
      text1.tag_add("gray", idx1, idx2)

def return_pressed (event):
  start = time.time()
  word = text2.get ("1.0", "end-1c")
  label1.config (text= " ● " + word)
  print (word)
  result = find_words (word)
  text1.delete ("1.0", END)
  text1.insert ("1.0", "".join (result))
  highlight (result,word)
  end = time.time()
  print (end - start) 
  text2.tag_add (SEL, "1.0", "end")
  text2.mark_set (INSERT, "1.0")
  text2.see (INSERT)
  return "break" # handled, do not send further!

def callback (sv,w):
  s = sv.get ()
  n = "".join ([c for c in s if c in "1234567890"])
  sv.set (n)
  set_max_m ()

def int_def (st,default=0):
  try:
    result = int (st)
  except ValueError:
    result = default
  return result

max_m = 200

def set_max_m ():
  global max_m
  max_m = int_def (spin1.get(),default=200)
  # print ("set_max_n", max_m)
  return_pressed (None)

root = Tk ()
root.title ('Cerca in dictionarios')

clr = "#a6f3cc"
fnt = ("Monospace", 9)

scroll1 = Scrollbar (root)
text1 = Text (
  root, height=40, bg=clr, bd=0, font=fnt, width=100, wrap=WORD)

frame1 = Frame (root)
text2 = Text (root, height=3, bg=clr, bd=0, font=fnt, width=100)
label1 = Label (
  frame1, bg=clr, bd=0, width=96, font=fnt, anchor=W, 
  justify=LEFT)
spinvar = StringVar (value=max_m)
spin1 = Spinbox (
  frame1,from_=0,to=5000,width=4,relief=FLAT,bd=0,
  buttondownrelief=FLAT,buttonuprelief=FLAT,increment=200,
  font=fnt, textvariable=spinvar,
  command=set_max_m)
spin1.delete(0, "end"); spin1.insert(0, max_m)
label1.pack (side=LEFT,fill=X)
spin1.pack (side=RIGHT)

text2.pack (side=BOTTOM, fill=X)

frame1.pack (side=TOP, fill=X)
scroll1.pack (side=RIGHT, fill=Y)
text1.pack (side=LEFT, fill=Y)

spinvar.trace('w', lambda name, index, mode, sv=spinvar: callback 
  (spinvar,spin1))
scroll1.config (command=text1.yview)
text1.config (yscrollcommand=scroll1.set)
text2.bind ('<Return>', return_pressed)
text2.focus ()

text1.tag_configure (
  "gray", foreground="#ffffff", background="#444444")
lines = read_args ()
root.mainloop ()

