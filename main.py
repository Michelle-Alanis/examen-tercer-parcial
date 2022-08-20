# Busqueda Binaria

import math

n = None
bandera = None
inicio = None
final = None
arreglo = None
x = None
centro = None

def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)


n = 12
bandera = False
inicio = 1
final = n
arreglo = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
x = float(text_prompt('¿Qué elemento desea buscar? '))
while bandera == False and inicio <= final:
  centro = math.floor((inicio + final) / 2)
  if x == arreglo[int(centro - 1)]:
    bandera = True
  else:
    if x < arreglo[int(centro - 1)]:
      final = centro - 1
    else:
      inicio = centro + 1
if bandera == True:
  print(''.join([str(x2) for x2 in ['El valor buscado ', x, ' se encuentra en la posición del índice ', centro]]))
else:
  print(''.join([str(x3) for x3 in ['El valor buscado ', x, ' no fue localizado en el arreglo de ', n, ' posiciones.']]))