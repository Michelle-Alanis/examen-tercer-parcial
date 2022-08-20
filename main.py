import math

arreglo = None
n = None
clave = None
respuesta = None
a = None
b = None
der = None
posicion = None
izq = None
mid1 = None
mid2 = None

# Describe this function...
def busqueda_ternaria(arreglo, n, clave):
  global respuesta, a, b, der, posicion, izq, mid1, mid2
  a = 0
  b = 0
  der = n
  izq = 1
  while b != 1:
    mid1 = round(izq + (der - izq) / 3)
    mid2 = round(der - (der - izq) / 3)
    if mid1 > 10 or mid2 > 10 or mid1 < 1 or mid2 < 1:
      b = 1
    else:
      if arreglo[int(mid1 - 1)] == clave:
        respuesta = mid1
        a = 1
        b = 1
      else:
        if arreglo[int(mid2 - 1)] == clave:
          respuesta = mid2
          a = 1
          b = 1
        else:
          if arreglo[int(mid1 - 1)] > clave:
            der = mid1 - 1
          else:
            if arreglo[int(mid2 - 1)] < clave:
              izq = mid2 + 1
            else:
              izq = mid1 + 1
              der = mid2 - 1
  if a == 0:
    respuesta = -1
  return respuesta

def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)


arreglo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 10
clave = float(text_prompt('¿Que elemento desea buscar?'))
posicion = busqueda_ternaria(arreglo, n, clave)
if posicion != -1:
  print(''.join([str(x) for x in ['El número ', clave, ' se encontró en la posición ', posicion]]))
else:
  print('Número no encontrado')