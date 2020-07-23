

from tkinter import *
import sys

# lines = ['line 1\n','line 2\n', 'line 3\n']

lines = []
n = len (sys.argv)
for i in range (1, n):
  filename = sys.argv[i]
  with open (filename) as f:
    lines = lines + f.readlines ()
print ("In toto",len (lines),"lineas")

def find_words (word):
  max_m = 200
  result = []
  if len (word) > 0:
    m = 0
    i = 0
    while m <= max_m and i < len (lines):
      s = lines [i]
      i = i + 1
      if word in s:
        result.append (s)
        m = m + 1
    if m > max_m: 
      result.append ("...")
  return result

def return_pressed (event):
  word = entry1.get ()
  result = find_words (word)
  entry1.delete (0, END)
  text1.delete ("1.0", END)
  text1.insert ("1.0","".join (result))

root = Tk ()
root.title ('Cerca in dictionarios')

svar = StringVar ()
entry1 = Entry (root, textvariable=svar, width=100)
scroll1 = Scrollbar (root)
text1 = Text (root, height=40, width=100)

entry1.pack (side=TOP, fill=X)
scroll1.pack (side=RIGHT, fill=Y)
text1.pack (side=LEFT, fill=Y)

scroll1.config (command=text1.yview)
text1.config (yscrollcommand=scroll1.set)
entry1.bind ('<Return>', return_pressed)
entry1.focus ()

root.mainloop ()

