# Salto de Busqueda

import math

a = None
b = None
arreglo = None
res1 = None
clave = None
n = None
bloque = None
previo = None
saltos = None
posicion = None

# Describe this function...
def min2(a, b):
  global arreglo, res1, clave, n, bloque, previo, saltos, posicion
  if b > a:
    res1 = a
  else:
    res1 = b
  return res1

def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)


arreglo = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
clave = float(text_prompt('¿Qué elemento desea buscar? '))
n = 16
bloque = math.floor(math.sqrt(n))
previo = 1
saltos = 1
while arreglo[int(min2(bloque, n) - 1)] < clave:
  previo = bloque
  bloque = bloque + math.floor(math.sqrt(n))
  saltos = saltos + 1
  if previo >= n:
    posicion = -1
while arreglo[int(previo - 1)] < clave:
  previo = previo + 1
  if arreglo[int(previo - 1)] == clave:
    posicion = previo
  else:
    posicion = -1
if posicion >= 0:
  print(''.join([str(x) for x in ['El numero ', clave, ' se encontró en la posicion ', posicion, ' con ', saltos, ' saltos de búsqueda.']]))
else:
  print(''.join([str(x2) for x2 in ['Se realizaron ', saltos, ' saltos para buscar el número ', clave, ' en el arreglo de longitud ', n, ', pero no fue encontrado.']]))