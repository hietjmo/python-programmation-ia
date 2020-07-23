# Files texto

In capitulo 2 nos preparava functiones a transformar numeros a sequentias de characteres. Nos definiva listas como `unes` e `deces`, e functiones como `milles`, `centos`, `unes1`, et cetera. Omnes le functiones nos salvava in file `numerales.py`.

Nos nunc pote utilisar file `numerales.py` in le interprete de Python. Ex functiones le function `numeral` es le plus utile, le alteres nos hodie non besonia. Si le file `numerales.py` es in le mesme directorio ubi nos initia le interprete, nos pote importar lo como un modulo:

```
> from numerales import numeral
> numeral (2020)
'duo milles vinti'
```

Nos construe le prime 50 mille numeros e salva los in file `numeros.txt`:

```
lines = []
for i in range (0,50_000):
  lines.append (f"{i}: {numeral(i)}\n")
with open ("numeros.txt","w") as f:
  f.writelines (lines)
```

Le file `numeros.txt` nunc ha 50 000 lineas de numeros:

```
0: zero
1: un
2: duo
3: tres
...
49999: quaranta-nove milles nove centos novanta-nove
```

## Le componente `Text`

Le componente `Text` in modulo `tkinter` es un campo de texto de plure lineas. Nos crea illo como le altere componentes in modulo `tkinter` (figura \ref{tk-text}).

\begin{figure}[]
\begin{center}
\includegraphics{figures/tk-text-1.png}
\caption{Componente Text.}
\label{tk-text}
\end{center}
\end{figure}


```
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
```

Nos da le focus al componente `entry1`, que es de typo `Entry`. Quando nos pressa le clavo `<Return>`, nos voca le function `return_pressed`.

```
entry1.bind ('<Return>', return_pressed)
entry1.focus ()
```

Nos defini le function `return_pressed` a vocar le function `find_words`, Le function que responde a function `bind` ha le evento como prime argumento. Hic nos tamen non usa le argumento `event`. Le texto que nos cerca, es in campo `entry1`. Le resultatos de cerca nos monstra in componente `text1`.

Le componente de typo `Text` es un campo de texto de plure lineas, e il existe differente formas a exprimer su indice, per exemplo `"linea.columna"` o `INSERT` o `END`. Le indice `"1.0"` es le prime columna de prime linea.

```
def return_pressed (event):
  word = entry1.get ()
  result = find_words (word)
  entry1.delete (0, END)
  text1.delete ("1.0", END)
  text1.insert ("1.0","".join (result))
```

Le function `find_words` cerca le texto inter le lineas, e da nos al maximo `max_m = 200` lineas como resultato. 

```
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
```

Quando nos initia le programma, Python ha le argumentos in lista `sys.argv`. Le prime elemento `sys.argv[0]` es sempre le nomine de programma. Nos usa le altere argumentos a leger le textos in lista `lines`.

```
import sys

lines = []
n = len (sys.argv)
for i in range (1, n):
  filename = sys.argv[i]
  with open (filename) as f:
    lines = lines + f.readlines ()
print ("In toto",len (lines),"lineas")
```

Le file `numeros.txt` como prime argumento le programma responde

```
# python tk-text.py numeros.txt
In toto 50000 lineas
```

