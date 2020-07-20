# Programma de numerales

In iste capitulo nos continua apprender le linguage Python per le exemplos de numerales de Interlingua.


## Le function `print`

Nos usa le function `print` a monstrar sequentias de characteres sur terminal texto.

Le function `print` pote haber argumentos de differente typos. Le interprete adde spatios inter cata argumento.

```
> print ("Un die ha",24*60*60,"secundas.")
Un die ha 86400 secundas.
```

Il es possibile da le clave `end` como argumento a function `print`. Le clave `end` es un sequentia de characteres addite in fin de texto.

Normalmente le function `print` adde in fin de texto un signo a cambiar le linea (`"\n"`). Ecce exemplos a usar le clave `end`:

```
> print (20, end=" "); print (20)
20 20
> print (20, end=""); print (20)
2020
```

## Le operator `in`

Le expression `(x in xs)` es `True`, quando `x` es un elemento de `xs`, e `False` alteremente.

```
> vocales = "eaiouy"
> "a" in vocales
True
> "t" in vocales
False
```

## Le instruction `for`

Le instruction `for` transverse un sequentia iterabile:

```
> for c in "eaiou":
|   print (c, end=' ')
| 
e a i o u
```

## Le instruction `if`

Le instruction `if` ha le forma

```
if expression_1:
  functiones_1
elif expression_2:
  functiones_2
else:
  functiones_3
```

ubi `functiones_1` es vocate quando `expression_1` es considerate ver. In altere caso le `functiones_2` de parte `elif` es vocate quando `expression_2` es ver, et cetera. Si cata expression es considerate false, le `functiones_3` de parte `else` es vocate. Le nomine `elif` veni ex le parolas anglese *else if*.

Un expression es considerate false quando il ha le valor `None`, `False`, `0`, `0.0`, `''`, `()`, `[]`, `{}`, et cetera. In altere casos le expression es considerate ver.

## Comprehensiones 

Un methodo a formar un lista de iterabiles, es usar *comprehensiones*. Comprehensiones es expressiones inter parentheses quadrate `[`...`]` con un o plure instructiones `for`, possibilemente con instructiones `if`.

```
> vocales = "eaiouy"
> [c for c in vocales]
['e', 'a', 'i', 'o', 'u', 'y']

> alfabeto = "eaionlsrtucdmpvbghfqxjykzw"
> consonantes = [c for c in alfabeto if c not in vocales]
> consonantes
['n', 'l', 's', 'r', 't', 'c', 'd', 'm', 'p', 'v', 'b', 'g', 'h', 
 'f', 'q', 'x', 'j', 'k', 'z', 'w']
```

## Generatores

*Generatores* es functiones que genera valores a *iterar*, id es, valores que nos pote transversar.

Le function `range` es un generator simple, que genera a nos sequentias arithmetic. Nos trova le forma de vocar de function `range` quando nos scribe `help (range)` al interprete:

```
> help (range)
class range(object)
 |  range(stop) -> range object
 |  range(start, stop[, step]) -> range object
...
```

Le valor de function `range` es talmente un objecto de `range`. Le argumento `start` es le comencio de sequentia, le argumento `stop` le fin. Le comencio es parte de sequentia, ma le fin non es: `(start <= x < stop)`.

- Le forma breve `range (stop)` da nos un objecto `range` de elementos de `0` a `(stop - 1)`. Le amonta de elementos es `stop`.

- Le forma `range (start,stop)` da nos un objecto `range` de elementos de `start` a `(stop - 1)`. Le amonta de elementos es `(stop - start)`.

- Le forma `range (start,stop,step)` da nos un objecto `range` de elementos de `start` a `(stop - 1)` con le intervallo `step`.

Le comprehensiones da nos un medio natural a representar elementos generate per `range`:

```
> [x for x in range (5)]
[0, 1, 2, 3, 4]
> [x for x in range (3,7)]
[3, 4, 5, 6]
> [x for x in range (1,11,2)]
[1, 3, 5, 7, 9]
> [x for x in range (5,-1,-1)]
[5, 4, 3, 2, 1, 0]
```

## Nomines de numerales: unes

In le lista `unes` nos ha definite le nomines de numeros 1...9.

```
unes = [ '', 'un', 'duo', 'tres', 'quatro', 'cinque', 
 'sex', 'septe', 'octo', 'nove' ]
```

Nos memora que le indice de un lista comencia per zero, e pro isto nos defini le prime elemento de nostre lista a un valor vacue (`''`). Nunc le altere numeros remane in su loco correcte:

```
> unes [0]
''
> unes [3]
'tres'
```

Le unes de un numero es sempre le residuo de division per 10. Per exemplo,

```
> 5764 % 10
4
```

Si le integre numero `n` es 0, le resultato es \"zero\".
Alteremente il existe parola pro unes solmente si `(n % 10 > 0)`. Nos defini le function `unes1`, que ha le argumento `n` (le numero integre).


```
def unes1 (n):
  i = n % 10
  result = ''
  if n == 0: 
    result = 'zero'
  elif i > 0:
    result = unes [i]
  return result
```


Si le numero integre es 3456, nos  ha \"sex"\ unes. Si le numero es 40, nos ha 0 unes, e nos non vole dicer \"quaranta-zero\". Solmente si le integre numero es 0, e nos ha 0 unes, le parola es \"zero\".

```
> unes1 (3456)
'sex'
> unes1 (40)
''
> unes1 (0)
'zero'
```

## Deces in un numeral

Le nomines a deces nos ha in lista `deces`. 

```
deces = [ '', 'dece', 'vinti', 'trenta', 'quaranta', 'cinquanta',
  'sexanta', 'septanta', 'octanta', 'novanta' ]
```

Le numero 3456 ha `(n % 100 // 10)`, id es, 5 deces, e talmente le parola es \"cinquanta\".

```
> deces [5]
'cinquanta'
```


## Centos in un numeral

Le numero integre `n` sempre ha `(n % 1000 // 100)` centos. Per exemplo,


```
> 3456 % 1000 // 100
4
> 12 % 1000 // 100
0
```

Quando nos ha 1 de centos, le parola pro isto es \"cento\". Quando nos ha plure de centos, nos adjunge le numeral de unes (\"duo\", \"tres\", \"quatro\", ...) al forma plural \"centos\". Nos anque debe haber un spatio inter le parolas. Le function `centos` deveni

```
def centos (n):
  c = n % 1000 // 100
  result = ''
  if c == 1:
    result = 'cento'
  if c > 1:
    result = unes [c] + ' centos'
  return result
```

Nunc per exemplo,

```
> centos (100)
'cento'
> centos (200)
'duo centos'
```

## Le union de centos, deces, e unes

Nos nunc ha le centos, le deces, e le unes de numero `n`:

```
c = centos (n)
d = deces [n % 100 // 10]
u = unes1 (n)
```

Quando nos adjunge le parolas, nos debe notar, que pote mancar alicun de parolas, atque etiam omnes de illos. Pro isto nos defini function `join_numwds`:

```
def join_numwds (a,b,sep=" "):
  result = ''
  if a and b:
    result = a + sep + b
  elif a:
    result = a
  elif b:
    result = b
  return result
```

Le function `join_numwds` ha un clave `sep` como argumento. Isto naturalmente es le *separator* inter parolas. Quando, per exemplo, le numero es \"cento un\", le separator es un spatio `' '`. Quando le numero es \"dece-duo\" le separator es un linea `'-'`. Usualmente le separator es un spatio, e pro isto argumento `sep` deveni le argumento predefinite con le valor `' '`. Isto significa que nos pote omitter le argumento quando illo ha le valor predefinite.

Le expression `(a and b)` deveni ver, quando et `a` et `b` ha un valor differente a un sequentia vacue `''`. Tunc nos adjunge sequentias `a`, `sep` et `b`.

Alteremente le resultato es `a` quando `a` existe, o `b` quando `b` existe. Si necuno existe, le resultato es un sequentia vacue `''`.

Alora, nos adjunge deces e unes per un linea `'-'` e le centos con le resultato de iste per un spatio `' '`. Nos memora que un spatio es argumento predefinite, e talmente nos pote omitter lo.

```
def from1to999 (n):
  c = centos (n)
  d = deces [n % 100 // 10]
  u = unes1 (n)
  w1 = join_numwds (d,u,"-")
  w2 = join_numwds (c,w1)
  return w2
```

## Milles

Quando nos calcula le milles de un numero, nos pote utilisar le function pro centos, deces e unes. Le numero `n` sempre ha `(n % 1_000_000 // 1_000)` milles. Per exemplo le numero 1000 ha un mille, le 5000 ha cinque milles e 123 000 ha cento vinti-tres milles. Le function pro 1, 5, e 123 es le mesme function `from1to999` que nos usava pro unes.

Le function `milles` nunc es

```
def milles (n):
  m = n % 1_000_000 // 1_000
  result = ''
  if m == 1:
    result = 'mille'
  if m > 1:
    result = from1to999 (m) + ' milles'
  return result
```

Hic nos vide que in Python nos pote gruppar le numeros con un tracto de sublineamento `_`, per exemplo un million deveni `1_000_000`.

## Le numero integre

Nos nunc ha omnes le partes pro calcular numeros de 0 a 999 999:

```
def numeral (n):
  m = milles (n)
  c = from1to999 (n)
  w = join_numwds (m,c)
  return w
```

Que nos testa le algorithmo per numeros aleatori!

## Le modulo `random`

Le modulo `random` produce numeros aleatori. 

Per exemplo le function `randint` da nos un numero integre inter duo numeros. Le function `random` da nos un numero de typo `float` inter 0 e 1.

Le function `choice` selige un elemento aleatori ex un lista. Le function `shuffle` misce le elementos de un lista.

```
> random.randint (1,3)
3
> random.random ()
0.8974826518988037
> random.choice ([3,5,7,9])
7
> t = ['A','B','C']
> random.shuffle (t)
> t
['C', 'A', 'B']
```

## Numerales aleatori in parolas

Le test de numerales aleatori deveni

```
for i in range (1,5):
  n = random.randint (0,20_000)
  print (n, numeral (n))
```

Le resultatos es

```
16631 dece-sex milles sex centos trenta-un
7650 septe milles sex centos cinquanta
4800 quatro milles octo centos
117 cento dece-septe
```

## Methodo `str.join`

Sequentias de characteres ha le methodo `join`, que adjunge le elementos de su argumento con le instantia de classe `str`. Per exemplo, `" ".join (["A","B","C"])` adjunge le elementos `"A"`, `"B"` et `"C"` con le sequentia `" "`.


```
> " ".join (["A","B","C"])
'A B C'
```

Quando nos vole colliger numeros ex un sequentia de characteres, nos pote utilisar comprehensiones e methodo `join`:

```
> s = "5i739iA39j55"
> "".join ([c for c in s if c in "1234567890"])
'57393955'
```

## Secunde programma graphic

Nos ha usate le componente `Label` a monstrar un texto in un fenestra. Nunc nos adde un componente `Entry` a leger un sequentia de characteres. 

Ambes ha un lista de proprietates que nos pote usar a cambiar le aspecto de elemento: su parente, color, bordo, largessa, typo de litteras, et cetera. Nos selige nulle bordo, texto nigre sur fundo blanc. Nomines de numerales es longe: nos selige largessa 60 characteres (figura \ref{entry-py}).

\begin{figure}[H]
\begin{center}
\includegraphics{figures/entry-py.png}
\caption{Nostre programma "Numerales".}
\label{entry-py}
\end{center}
\end{figure}

Quando le fenestra appare, nos da le focus al componente `Entry`, post que nos pote scriber in fenestra sin cliccar le componente.

```
root = Tk ()
root.title ('Numerales')
sv = StringVar ()
e = Entry (root, textvariable=sv, bd=0, width=60)
w = Label (root, bg="white", fg="black", width=60)
e.pack ()
w.pack ()
sv.trace ("w", lambda name, index, mode, sv=sv: callback (sv,w))
e.focus_set ()
root.mainloop ()  
```

Hic nos ha prestate un function `callback`, que responde al cambios de texto. Le texto es in variabile `sv` de classe `StringVar`. Nos lege le texto per methodo `get`.

Nos sape como colliger le numeros ex texto. Quando nos scribe solmente le numeros, nos ha validate le entrata.

```
def callback (sv,w):
  s = sv.get ()
  n = "".join ([c for c in s if c in "1234567890"])
  sv.set (n)
  numero = intA (n)
  if numero < 1_000_000: 
    result = numeral (numero)
  else: 
    result = 'troppo'
  t = str (intA (n)) + ": " + result
  print (t)
  w ['text'] = t
```

Nos ancora defini un function `intA` que sempre retorna un numero integre. Si le sequentia de characteres non es un numero, nos ha un error (plus exacte un `ValueError`). Tunc nos retorna un valor predefinite per clave `default`. Un tal error eveni in nostre caso quando le sequentia de characteres es vacue `''`.


```
def intA (st,default=0):
  try:
    result = int (st)
  except ValueError:
    result = default
  return result
```


