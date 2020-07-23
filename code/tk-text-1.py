

from tkinter import *

root = Tk ()
root.title ('Fenestra Tkinter')

svar = StringVar ()
entry1 = Entry (root, textvariable=svar, width=50)
scroll1 = Scrollbar (root)
text1 = Text (root, height=3, width=50)

entry1.pack (side=TOP, fill=X)
scroll1.pack (side=RIGHT, fill=Y)
text1.pack (side=LEFT, fill=Y)

scroll1.config (command=text1.yview)
text1.config (yscrollcommand=scroll1.set)

svar.set ("Entry widget")
txt = "Text widget\n...\n...\n"
text1.insert (END,txt)

root.mainloop ()

