primera_tupla = 23,55,43
print(primera_tupla)

segunda_tupla = 44,primera_tupla,23
print(segunda_tupla)

print(primera_tupla[2])
print(primera_tupla)

primera_lista = ['a','b','c']

tercera_tupla = (34,22,primera_lista,1)
print(tercera_tupla)
primera_lista[1] = 63
print(tercera_tupla)
tercera_tupla[2][0] = 'z'
print(tercera_tupla)