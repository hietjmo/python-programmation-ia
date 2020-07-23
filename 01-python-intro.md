# Linguage Python

Python es un linguage de programmation facile a apprender, moderne et effective. Le linguage es orientate a objectos e ha syntaxe de alte nivello. Il ha typage dynamic e character interpretate.

## Le interprete interactive

Nos initia le interprete de Python per le commando

```
python
```

Al comencio le interprete scribe a nos su version de programma e attende nostre instructiones.

```
# python
Python 3.8.3 (default, May 29 2020, 00:00:00) 
[GCC 10.1.1 20200507 (Red Hat 10.1.1-1)] on linux
> 
```

## Operatores arithmetic

Nos trova que le interprete de Python functiona ben como calculator.
Operatores arithmetic basic es `+`, `-`, `*` et `/`. Le operatores `*` et `/` ha plus alte prioritate que le operatores `+` et `-`, ma nos pote scriber expressiones in parentheses `(`...`)` pro cambiar le ordine de calculation. Le operator a elevar in potentia es `**`.


```
> 2 + 2
4
> 50 - 5 * 6
20
> 3 * (5 - 2)
9
> 2 ** 8
256
```

Le division (`/`) sempre resulta in numero decimal de classe `float`. Le operatores `//` et `%` da nos le quotiente e le residuo de division de numeros integre. Le numeros integre ha le typo `int`, in altere parolas, illes es de classe `int`.

```
> 8 / 5
1.6
> 11 // 4
2
> 11 % 4
3
```

## Valores veritate

Le valores veritate es `False` e `True`. Operationes boolean basic es `and`, `or`, e `not` (tabella \ref{tab:bool-basic}).

\begin{table}[H]
\caption{\label{tab:bool-basic}Operationes boolean.}
\begin{tabular}{p{1.0cm} | p{1.0cm}} 
{\ttfamily not} 	&\\
\hline
{\ttfamily False} 	& {\ttfamily True} \\
{\ttfamily True} 	& {\ttfamily False}  \\
\end{tabular}%
\quad
\begin{tabular}{p{1.0cm} | p{1.0cm} p{1.0cm}}
{\ttfamily and} 	& {\ttfamily False} & {\ttfamily True} \\
\hline
{\ttfamily False} & {\ttfamily False} 	& {\ttfamily False} \\
{\ttfamily True} 	& {\ttfamily False} & {\ttfamily True}  \\
\end{tabular}%
\quad
\begin{tabular}{p{1.0cm} | p{1.0cm} p{1.0cm}}
{\ttfamily or} 	& {\ttfamily False} & {\ttfamily True} \\
\hline
{\ttfamily False} & {\ttfamily False} 	& {\ttfamily True} \\
{\ttfamily True} 	& {\ttfamily True} & {\ttfamily True}  \\
\end{tabular}
\end{table}

Per exemplo,

```
> not False
True
> False and True
False
> False or True
True
```

Operatores a comparar es `<`, `>`, `==`, `<=`, `>=`, e `!=` (tabella \ref{tab:op-comp}).

Operator   Signification
---------  ------------------------
`<`        minor que
`>`        major que
`==`       equal a
`<=`       minor que o equal a
`>=`       major que o equal a
`!=`       inequal a
---------  ------------------------

: Operatores a comparar. \label{tab:op-comp}

Per exemplo,

```
> 3 < 4 < 5                      #         __                   
True                             #     ___( o)>        
> 10 + 10 != 20                  #     \ <_. )        >(.)__  
False                            #      `---'          (___/ 
```

## Sequentias de characteres

Sequentias de characteres pote esser representate inter virgulettas singule (`'`...`'`) o inter virgulettas duple (`"`...`"`). Le character a escappar es barra oblique inverse (`\`).

```
> 'Python' == "Python"
True
> 'Monty\'s' == "Monty's"
True
```

Le operatores `+` et `*` adjunge e repete sequentias de characteres.

```
> 'i' + 3 * 'nte'
'intentente'
```

Quando inter sequentias de characteres existe solmente spatio blanc, le interprete adjunge le sequentias.

```
> "inter"   "lingua"
'interlingua'
```

Il es possibile a trenchar un sequentia de characteres per su indices. Le prime character ha le indice zero. Le indice negative calcula de fin.

```
> t = 'Python'
> t [2:6], t [4:], t [-3:-1], t [-2:], t [-1]
('thon', 'on', 'ho', 'on', 'n')
```

## Listas

Un *lista* es un collection de valores scribite inter parentheses quadrate `[`...`]`. Nos defini un lista de nomines de numeros cardinal:

```
numeros = [ 'zero', 'un', 'duo', 'tres', 'quatro', 'cinque', 
 'sex', 'septe', 'octo', 'nove', 'dece' ]
```

Nos trova le *elementos* per le indices. Indices de un lista comencia de zero. Le `[]` es un lista vacue, e `[1]`, per exemplo, es un lista con un elemento.

```
> numeros [0]
'zero'
> numeros [5]
'cinque'
```

Nos anque pote trenchar le lista per le indices. 

```
> numeros [3:7]
['tres', 'quatro', 'cinque', 'sex']
```

## Dictionarios

Un dictionario consiste de pares de forma *clave*`:`*valor* scribite inter parentheses crispe `{`...`}`.

```
nums = { 
  'un': 1,  'duo': 2,   'tres': 3, 'quatro': 4, 'cinque': 5, 
  'sex': 6, 'septe': 7, 'octo': 8, 'nove': 9,   'dece': 10 }
```

Nos trova le valor per su clave.

```
> nums ["cinque"]
5
```

## Tuplas

Un $n$-*tupla* es un sequentia de $n$ valores. In Python nos scribe tuplas in parentheses `(`...`)`, per exemplo, `t = (1,2)`, o nos pote omitter le parentheses: `t = 1,2`. Le `()` es un 0-tupla, e `(2,)` es un 1-tupla.


Quando le formas es favorabile, il es possibile a dispacchettar le elementos de un tupla, per exemplo `(a,b) = t`. 

```
> p = 1,2
> a,b = p
> a
1
> b
2
```

## Variabiles e definitiones de functiones

Nos dice que le *sequentia Fibonacci* es le numeros 0 et 1 e sempre le summa de duo ultime numeros.

Nos pote definir un function `fibonacci (n)`, que calcula le `n` prime numeros de un sequentia Fibonacci:

```
def fibonacci (n):
  result = []
  a,b = 0,1
  while (len (result) < n):
    result.append (a)
    a,b = b, a+b
  return result
```

Nos voca le function per valor `n = 10`. Le resultato es un lista de 10 elementos:

```
> fibonacci (10)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

Hic le predefinite function `len (xs)` retorna le longor de lista (o sequentia) `xs`. Le listas ha un *methodo* `append (a)`, que adjunge le elemento `a` a un lista. 

```
> len ('interlingua')
11
> xs = []
> xs.append (4)
> xs
[4]
```

## Programma graphic con modulo `tkinter`

Nos nunc es preste a scriber nostre prime programma graphic. Pro isto nos usa le modulo venerabile `tkinter`. Nos salva le texto in  file `hello.py`.

```
from tkinter import *

root = Tk ()
label1 = Label (root, text="Salute Mundo!")
label1.pack ()
root.mainloop ()
```

Nos lancea le programma per commando `python hello.py`. In figura \ref{hello-py} nos vide qual es su aspecto.

\begin{figure}[H]
\begin{center}
\includegraphics{figures/hello.png}
\caption{Nostre prime programma graphic.}
\label{hello-py}
\end{center}
\end{figure}

## Importar modulos

In Python *modulos* son collectiones de *nomines*, id es, functiones e structuras de datos. Quando nos vole usar iste nomines, nos debe *importar* le modulo correspondente.

Il existe differente manieras a importar un modulo. Si le nomine de un modulo es `modulo` e illo ha functiones `f1`, `f2`, ..., nos pote importar le modulo per

- `import modulo`; post que nos voca functiones per nomines `modulo.f1`, `modulo.f2`, et cetera.

- `import modulo as md`; post que nos voca functiones per nomines `md.f1`, `md.f2`, et cetera.

- `from modulo import (f1,f2)`; post que nos pote usar le functiones listate (hic `f1` e `f2`) sin le nomine de modulo.

- `from modulo import *`; post que nos pote usar omnes le functiones de modulo sin le nomine de modulo. 

In modulo `math` nos trova functiones e structuras mathematic, per exemplo, le constantes `e` et `pi`. 

Ecce le prime forma a usar nomines:

```
import math
> math.e
2.718281828459045
> math.pi
3.141592653589793
```

Hic un altere forma:

```
> from math import *
> e
2.718281828459045
> pi
3.141592653589793
```

