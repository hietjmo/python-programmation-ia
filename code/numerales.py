
unes = [ '', 'un', 'duo', 'tres', 'quatro', 'cinque', 
 'sex', 'septe', 'octo', 'nove' ]

deces = [ '', 'dece', 'vinti', 'trenta', 'quaranta', 'cinquanta',
  'sexanta', 'septanta', 'octanta', 'novanta' ]

def milles (n):
  m = n % 1_000_000 // 1_000
  result = ''
  if m == 1:
    result = 'mille'
  if m > 1:
    result = from1to999 (m) + ' milles'
  return result

def centos (n):
  c = n % 1000 // 100
  result = ''
  if c == 1:
    result = 'cento'
  if c > 1:
    result = unes [c] + ' centos'
  return result

def unes1 (n):
  i = n % 10
  result = ''
  if n == 0: 
    result = 'zero'
  elif i > 0:
    result = unes [i]
  return result

def join_numwds (a,b,sep=" "):
  result = ''
  if a and b:
    result = a + sep + b
  elif a:
    result = a
  elif b:
    result = b
  return result

def from1to999 (n):
  c = centos (n)
  d = deces [n % 100 // 10]
  u = unes1 (n)
  w1 = join_numwds (d,u,"-")
  w2 = join_numwds (c,w1)
  return w2

def numeral (n):
  m = milles (n)
  c = from1to999 (n)
  w = join_numwds (m,c)
  return w


