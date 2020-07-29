# Classes

*Classes* da nos un instrumento a unir le datos e le functionalitate. Quando nos crea un nove classe, nos crea un nove *typo* de objecto, e nos pote crear nove *instantias* de iste typo. Cata instantia de un classe pote haber *attributos*, id es, characteristicas proprie a un objecto, que mantene le *stato* del objecto. Instantias de classe pote anque haber *methodos* pro modificar le stato del objecto.

## Le classe minimal

Nostre prime classe a definir es un classe minimal, `A`, a que nos non defini ni methodos ni attributos:

```
class A:
  pass
```

Le instruction `pass` dice a facer nihil. --- Isto es un classe minimal.

Nos defini un instantia `a` de classe `A`.

```
> a = A ()
```

Nos pote definir le nomines `a.x` et `a.y`:

```
> a.x = 4
> a.y = 1
> a.x, a.y
(4, 1)
```

## Le attributos e methodos

Quando nos crea objectos, nos defini le valores initial al attributos de objectos in methodo `__init__`.

```
class B:
  def __init__ (self, x, y):
    self.x = x
    self.y = y
```

Cata definition de un methodo ha `self` como prime argumento. Isto es un formalitate a facer le objecto mesme usabile a methodo. 

Nos crea un objecto `b` de classe `B`, con initial valores `x = 3` et `y = 4`:

```
> b = B (3,4)
```

In le definition de classe, nos defini le methodo `methodo_x`. Le definition ha al minus un argumento, `self`, le objecto mesme:

```
  ...
  def methodo_x (self):
    pass
  ...
```

Nos voca le methodo. Nunc le argumento `self` ha le valor `self = b`.

```
b.methodo_x ()
```

Si nos vole, nos pote initiar `x` et `y`, per exemplo, a valores `x = 0` et `y = 0` (puncto origine).

```
class C:
  def __init__ (self, x=0, y=0):
    self.x = x
    self.y = y
```

Nos defini un instantia `c` de classe `C`. Le instantia nunc ha le attributos `x` et `y`, con valores `c.x = 0` et `c.y = 0`.

```
> c = C ()
> c.x, c.y
(0, 0)
```

## Le classe `Point`

Nos nunc defini un classe `Point` que es simile a classes `A`, `B`, et `C` supra, ma que ha anque altere methodos:

```
class Point:
  def __init__ (self, x=0, y=0):
    self.x = x
    self.y = y
  def __repr__ (self):
    return f"Point ({self.x},{self.y})"
  def pair (self):
    return (self.x,self.y)
```

Le methodo `__repr__` es le *representation* de un objecto de classe in question. Nos vide iste representation quando nos scribe le nomine de un objecto in interprete interactive:

```
> p = Point ()
> p
Point (0,0)
```

Nos anque definiva un methodo `pair`, que retorna a nos un 2-tupla con le coordinatas `(x,y)`.

```
> p.pair ()
(0, 0)
```

## Le classes `Line` e `Polygon`

Nos defini un objecto de classe `Line` per duo punctos `p1` et `p2`. Un objecto de classe `Polygon` ha un attributo `ps` que es un lista de punctos.

```
class Line: 
  def __init__ (self, p1, p2):
    self.p1 = p1
    self.p2 = p2

class Polygon:
  def __init__ (self, ps):
    self.ps = ps
```

## Le f-formato de sequentias de characteres

Le *f-formato* es un maniera de formation de sequentias de characteres.

Nos scribe le littera `f` o `F` ante le prime virguletta, e le expressiones inter parentheses crispe `{`...`}`. Il ha differente manieras a manipular le aspecto de sequentia, per exemplo `f"{x:.2f}"` da le valor de `x` con 2 decimales.

```
> twopi = 6.2831853
> f"Le perimetro de circulo unitate es circa {twopi:.2f}."
'Le perimetro de circulo unitate es circa 6.28.'
> a,b = 6,7
> f"{a} vices {b} es {a*b}."
'6 vices 7 es 42.'
```

## Modulo `cairo`

Nos usa le  modulo `cairo` a pinger picturas. Iste vice nos face un pictura de formato PDF. Prime nos crea un contexto `ct` a pinger. Nos face le area vacue quando nos pinge un rectangulo blanc de puncto $(0,0)$ al angulo opposite de pictura.

Le modulo `cairo` ha le functiones a pinger rectangulos, a eliger un color, e a plenar un forma con le color. Le functiones es le methodos `rectangle`, `set_source_rgb`, e `fill` de instantias de classe `cairo.Context`.

```
w_pic, h_pic = 170,130
w,h = 160,120
filename = "armature-1.pdf"
surface = cairo.PDFSurface (filename, w_pic, h_pic)
ct = cairo.Context (surface)

ct.rectangle (0, 0, w_pic, h_pic)
ct.set_source_rgb (1.00, 1.00, 1.00)
ct.fill()
```

Nos defini functiones `draw_rect`, `draw_line`, e `draw_polygon` a pinger un rectangulo, un linea, e un polygono. Nos nunc besonia le methodos `move_to`, `line_to` e `close_path` de nostre objecto `ct`.

```
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
```

Nos nunc pinge le pictura (figura \ref{pic-diagonal}):

```
x1,y1 = 5,5
x2,y2 = x1 + w, y1 + h

pairs1 = [(x1,y1),(x2,y1),(x2,y2),(x1,y2)]
ps = [Point (a,b) for (a,b) in pairs1]

draw_line (Line (ps[0],ps[2]))
draw_rect (ps[0],ps[2])

ct.set_source_rgb (0.00, 0.00, 0.00)
ct.set_line_width (1.0)
ct.stroke ()
```

\begin{figure}[]
\begin{center}
\includegraphics{figures/armature-2.pdf}
\caption{Pictura con un rectangulo e un diagonal.}
\label{pic-diagonal}
\end{center}
\end{figure}

## Modulo `subprocess`

Nos pote monstrar le pictura per un visualisator externe. Hic nos usa le programma `mupdf`. Le modulo `subprocess` ha function `Popen` a initiar un processo externe.

```
import subprocess

filename = "armature-1.pdf"
subprocess.Popen (["mupdf " + filename],shell=True)
```

## Intersection de duo lineas

Nos defini un function `intersection` que calcula le puncto de intersection inter duo lineas. 

```
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
```

Hic nos trova un maniera a scriber sequentias de characteres que contine saltos de lineas: le virgulettas triple, `'''`...`'''` o `"""`...`"""`. In le prime linea de un definition illos forma un documentation pro definition, que nos vide scribente `help (intersection)` e que es situate in attributo `intersection.__doc__`.

```
> intersection.__doc__
'Line-Line intersection\n\n  From: en.wikipedia.org/...\n  '
```

Nos anque defini un function `draw_point` a pinger un puncto.

```
def draw_point (pt):
  ct.arc (pt.x,pt.y,3,0,math.tau)
  ct.set_source_rgb (0, 0, 0)
  ct.fill ()
```

Nos pinge le diagonales del rectangulo, e calcula lor puncto de intersection.

```
diagonal1 = Line (ps[0],ps[2])
diagonal2 = Line (ps[1],ps[3])

draw_line (diagonal1)
draw_line (diagonal2)

c1 = intersection (diagonal1,diagonal2)
```

Finalmente nos pinge le punctos (figura \ref{pic-punctos}). Hic `ps` es un lista de punctos, e nos pote usar le operator `+` a unir duo listas, quando le ambe operandos es listas: puncto `c1` deveni lista per parentheses quadrate `[c1]`.

```
for p in ps + [c1]:
  draw_point (p)
```

\begin{figure}[]
\begin{center}
\includegraphics{figures/armature-4.pdf}
\caption{Diagonales de un rectangulo e punctos de intersection.}
\label{pic-punctos}
\end{center}
\end{figure}



## Operator `+` inter duo objectos

Similarmente que nos definiva methodo `__repr__` a un objecto, nos pote definir le operator `+` a adder duo objectos. Le methodo a definir es `__add__`. In `a + b` le prime operando `a` a adder deveni le argumento `self`. Le secunde operando `b` deveni le argumento secunde: `__add__ (self, b)`. 

Hic nos defini addition inter duo punctos, id es, inter duo objectos de classe `Point`:

```
class Point:
  ...
  def __add__ (self, p2):
    return Point (self.x + p2.x, self.y + p2.y)
  ...
```

Nunc le addition de duo objectos es le addition de su vectores de position.

```
> a = Point (1,2)
> b = Point (3,4)
> a + b
Point (4,6)
```

Le centro inter duo punctos es

```
def center (a,b):
  return Point ((a.x + b.x) / 2, (a.y + b.y) / 2)
```

## Le function `enumerate`

Le function `enumerate` es un generator que numera un sequentia:

```
> list (enumerate ("eaiou"))
[(0, 'e'), (1, 'a'), (2, 'i'), (3, 'o'), (4, 'u')]
```

Usante un numeration, nos trova le indices de un lista, e nos pote facer calculationes per illos. Per exemplo, un circulo al transverso de indices de lista `v = "ABCD"` es

```
> [(v [i],v [(i+1) % len (v)]) for i,e in enumerate (v)]
[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')
```

Le longor `len (v)` de lista `v` es 4, e le function `enumerate` da al variabile `i` le valores 0...3. Quando `i = 3` le indice `(i+1)` es $3+1=4$ e $4 \;\mathrm{mod}\; 4 = 0$. Le ultime elemento `(v [3], v [0])` nunc es `('D', 'A')` que completa le circulo.

## Insimules

In Python un *insimul* (anglese: *set*) adhere le notation de parentheses crispe `{`...`}` de un dictionario. Le elementos de un insimul tamen es valores, e non de forma *clave*`:`*valor*. Le `set ()`
es un insimul vacue. (Le `{}` es un dictionario vacue.)

```
> type ({})
<class 'dict'>
> type (set ())
<class 'set'>
```

Nos usa insimules quando nos vole que cata elemento del insimul es unic.

```
> {1,2,1,3,2,4}
{1, 2, 3, 4}
```

## Lineas inter cata puncto

Nos ha le centros inter punctos `ps` in lista `cs`: 

```
cs = [center (ps[i],ps[(i+1)%len(ps)]) for i,e in enumerate (ps)]
```

Nos prende un elemento per vice de ambe lista, e extende le nove lista `ts` correspondente.

```
ts = []
for (a,b) in zip (ps,cs):
  ts.extend ([a,b])
```

Quando nos trencha le lineas per centros, alicun de illes veni superflue:

```
cutd = [(0,2),(2,4),(4,6),(0,6)]
```

Nos nunc ha un bon comprehension in forma de un insimul `s1`:
 
```
t = range (len (ts))
s1 = {(a,b) for a in t for b in t if a < b if (a,b) not in cutd}
ks = [Line (ts[a],ts[b]) for (a,b) in s1]
```

Quando nos pinge le lineas e le punctos, nos trova un nove pictura (figura \ref{pic-armatura-5}).

```
for k in ks:
  draw_line (k)
ct.stroke ()

for p in ts:
  draw_point (p)
```

\begin{figure}[]
\begin{center}
\includegraphics{figures/armature-5.pdf}
\caption{Lineas inter punctos.}
\label{pic-armatura-5}
\end{center}
\end{figure}


