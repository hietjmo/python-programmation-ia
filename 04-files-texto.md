# Operationes a files texto

In capitulo 2 nos preparava functiones a transformar numeros a sequentias de characteres. Nos definiva listas como `unes` e `deces`, e functiones como `milles`, `centos`, `unes1`, et cetera. Omnes le functiones nos salvava in file `numerales.py`.

Nos nunc pote utilisar file `numerales.py` in le interprete de Python. Ex le functiones in file `numerales.py` nos vole usar le function `numeral`. Si le file `numerales.py` es in le mesme directorio ubi nos initia le interprete, nos pote importar lo como un modulo:

```
> from numerales import numeral
> numeral (2020)
'duo milles vinti'
```

Nos construe le prime 50 milles numeros e salva los in file `numeros.txt`:

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

Le objecto `Text` in modulo `tkinter` es un campo de texto de plure lineas. Un objecto `Text` usualmente anque besonia un barra a rolar. Nos crea un objecto `Scrollbar` pro isto. Nos connecte logicas de ambes per methodos `config`.

Le componente `entry1` ha su loco in supra de fenestra `(side=TOP)`, le componente `scroll1` in derecta `(side=RIGHT)`, e le componente `text1` in sinistre `(side=LEFT)` (figura \ref{tk-text}).

\begin{figure}[]
\begin{center}
\includegraphics{figures/tk-text-1.png}
\caption{Duo differente campos pro texto e un barra a rolar.}
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

Le componente de typo `Text` es un campo de texto de plure lineas, e il existe differente formas a exprimer su indice, per exemplo `"linea.columna"` o `INSERT` (puncto de insertion) o `END` (fin del texto). Le indice `"1.0"` es le prime columna de prime linea. (Le indices de linea comencia per 1, le indices de columna per 0.)

Nos selige le texto in campo `entry1`. Talmente illo dispare quando nos comencia scriber le sequente parola a cercar.

```
def return_pressed (event):
  word = entry1.get ()
  result = find_words (word)
  text1.delete ("1.0", END)
  text1.insert ("1.0","".join (result))
  entry1.selection_range(0, END)
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

## Argumentos del programma

Quando nos initia le programma, Python ha le argumentos in lista `sys.argv`. Le prime elemento `sys.argv [0]` es sempre le nomine de programma. Nos usa le altere argumentos a leger le textos in lista `lines`.

```
import sys

lines = []
arguments = sys.argv
for i,e in enumerate (arguments):
  print (f"{i}: {e}")
  if i > 0:
    filename = arguments[i]
    with open (filename) as f:
      lines = lines + f.readlines ()
print ("In toto",len (lines),"lineas")
```

Le file `numeros.txt` como prime argumento le programma responde

```
# python tk-text.py numeros.txt
0: tk-text.py
1: numeros.txt
In toto 50000 lineas
```

## Coloration de resultatos

Il es possibile a transformar le aspecto de partes individual del texto in componente `Text`. Un tal parte ha le nomine *etiquetta* (in anglese: *tag*).

Nos defini un forma de etiquetta `"gray"`.

```
text1.tag_configure (
  "gray", foreground="#ffffff", background="#444444")
```

In le function `return_pressed` nos ha le variabiles `word` e `result` que nos besonia a colorar le resultatos per function `highlight`:

```
def return_pressed (event):
  word = entry1.get ()
  result = find_words (word)
  ...
  highlight (result,word)
  ...
```

Le function `highlight` voca a generator `find_all`. Nos defini le generator `find_all` a dar nos le indices del etiquettas a colorar. Le indice `idx1` es le comencio e le indice `idx2` le fin. Le formato de indices `idx1` e `idx2` pro columna `x` in linea `y` es `"x.y"`. Le fin es le comencio addite a longor de etiquetta.

```
def highlight (result,word):
  for i,n in enumerate (result):
    for idx in find_all (n,word):
      idx1 = f"{i+1}.{idx}"
      idx2 = f"{i+1}.{idx+len (word)}"
      text1.tag_add("gray", idx1, idx2)
```

Nos defini le generator `find_all`. Su argumentos es le linea plen `s` e le parte `sub` que nos cerca. Le function `str.find` da nos le indice de prime sequentia trovate. Su argumentos es le parte `sub` que nos cerca e un indice `start` (un numero integre) de sequentia ubi nos comencia a cercar. Si le parte non es trovate, le resultato es $-1$.

Un generator es un function ordinari, excepte le valores que lo genera. Le generator retorna le valor in torno in instruction `yield`. Quando le proxime valor es necesse, le generator continua in le loco presto post le instruction `yield`.

```
def find_all (s,sub):
  start = 0
  while True:
    start = s.find (sub,start)
    if start == -1: return
    yield start
    start = start + len (sub) 
```

In figura \ref{tk-duo} nos ha cercate le parola \"duo\" in file `numeros.txt`.

\begin{figure}[]
\begin{center}
\includegraphics{figures/cerca-duo.png}
\caption{Le parola ''duo'' cercate.}
\label{tk-duo}
\end{center}
\end{figure}


## Calcular le frequentia de litteras

Pro calcular le frequentia de litteras in un sequentia, nos defini le function `letter_frequency`:

```
def letter_frequency (str1):
  dict = {}
  for n in str1:
    keys = dict.keys ()
    if n in keys:
      dict [n] += 1
    else:
      dict [n] = 1
  return dict
```

In le function nos ha un dictionario vacue `dict = {}`. Nos transversa le argumento `str1` littera post littera. Si le littera `n` non es in dictionario, nos da al clave `n` le valor 1. Si le littera `n` jam es in dictionario, nos augmenta su valor per 1.

Nunc, per exemplo,

```
> letter_frequency ('interlingua')
{'i': 2, 'n': 2, 't': 1, 'e': 1, 'r': 1, 'l': 1, 'g': 1, 'u': 1, 
 'a': 1}
```

Ma pro calcular frequentias, le modulo `collection` ha un objecto `Counter`, que es plus efficace (circa a factor $3x$):

```
> from collections import Counter
> cnt = Counter ('interlingua')
> cnt
Counter({'i': 2, 'n': 2, 't': 1, 'e': 1, 'r': 1, 'l': 1, 'g': 1, 
  'u': 1, 'a': 1})
> cnt.most_common ()
[('i', 2), ('n', 2), ('t', 1), ('e', 1), ('r', 1), ('l', 1), 
  ('g', 1), ('u', 1), ('a', 1)]
```

Per exemplo, nos pote leger un integre file e calcular le frequentia de characteres per

```
with open ('collection-1.txt') as f:
  content = f.read()

cnt = Counter (content)
```

Le methodo `most_common` da nos le plus sovente characteres.

```
> cnt.most_common (10)
[(' ', 54515), ('e', 38472), ('a', 25888), ('o', 20280), 
 ('i', 17807), ('l', 17360), ('n', 16270), ('s', 16200), 
 ('r', 15562), ('t', 14063)]
```

Le functiones a converter in minuscules e majuscules es `str.lower` e `str.upper`.
Post converter in minuscules, le litteras de interesse a nos es le litteras inter `"a"` et `"z"`. A calcular le summa per function `sum` nos prende de elemento `[(k,v)]` le valor `v`, id es, le parte `x [1]` ex le 2-tupla `x`.

```
ltrs = [c for c in content.lower() if "a" <= c <= "z"]
cnt = Counter (ltrs)
mc = cnt.most_common ()
total = sum ([x [1] for x in mc])
ratios = [(k, v / total) for (k,v) in mc]
prt_rt = [f"{k.upper()} {v:.4f}" for (k,v) in ratios]

print (prt_rt)
```

Nos presenta le numero total in gruppas de tres.

```
def g3 (number): 
  return ''.join (reversed (
    [x + (' ' if i and not i % 3 else '') 
     for i, x in enumerate (reversed (str (number)))]))

print ("Total:",g3 (total))
```

Le resultato es

```
['E 0.1568', 'A 0.1064', 'O 0.0820', 'I 0.0763', 'L 0.0715', 
 'S 0.0662', 'N 0.0662', 'R 0.0633', 'T 0.0574', 'U 0.0425', 
 'C 0.0385', 'D 0.0322', 'V 0.0320', 'M 0.0299', 'P 0.0289', 
 'B 0.0115', 'Q 0.0112', 'G 0.0081', 'H 0.0078', 'F 0.0071', 
 'J 0.0019', 'X 0.0016', 'Y 0.0005', 'K 0.0001', 'Z 0.0000', 
 'W 0.0000']
Total: 249 115
```

## Files CSV

Nos salva le resultato como un file CSV. Le file CSV (*comma-separated values*) es un file texto, que usualmente ha campos separate per commas e per signos a cambiar le linea.

Nos ha un lista de le plus sovente characteres in variabile `mc`. Nos arrangia lo in forma acceptabile a un scriptor CSV. Nos separa le campos per un signo de tabulator `'\t'`.

```
rows = [[k, v] for (k,v) in mc]
csvfile = "freq-collection-1.csv"

with open (csvfile, 'w') as f:
  writer = csv.writer (f,delimiter='\t')
  writer.writerows (rows)

print ("Wrote", csvfile)
```

## Modulo `matplotlib`

Post que nos ha salvate le resultatos in file CSV, nos lege illos pro monstrar un graphico. 

```
import csv

csvfile = "freq-collection-1.csv"

ltrs = []
amount = []

with open (csvfile) as f:
  reader = csv.reader (f,delimiter='\t')
  for row in reader:
    ltrs.append (row [0].upper())
    amount.append (int (row [1]))

total = sum (amount)
ratios = [n / total for n in amount]
```

Nos usa modulo `matplotlib` pro facer le graphico. Le resultato nos vide in figura \ref{freq-collection}.

\begin{figure}[]
\begin{center}
\includegraphics{figures/freq-collection-1.pdf}
\caption{Frequentia de litteras.}
\label{freq-collection}
\end{center}
\end{figure}


```
import matplotlib.pyplot as plt

f = plt.figure (figsize=(5.66,2.5))
bars = plt.bar (
  x=ltrs, height=ratios, color=(1,1,1,1), linewidth=1.0, 
  edgecolor='black')

bottom, top = plt.ylim ()
plt.ylim (top=top + 0.01)
for rect, label in zip (bars, ltrs):
  height = rect.get_height()
  x = rect.get_x () + rect.get_width () / 2
  y = height + 0.0015
  plt.text (x, y, label, ha='center', va='bottom')

plt.tick_params (bottom=False,labelbottom=False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
f.savefig ("freq-collection-1.pdf", bbox_inches='tight')
plt.show ()
```



