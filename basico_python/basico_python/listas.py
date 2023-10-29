
primera_lista = [32,45,76,23,6,86]
print(primera_lista)
print("Numero de elementos:",len(primera_lista))

segunda_lista = ["Alfa",True,12.3,1235,-23.5,0.005,9.00004]
print(segunda_lista)
print("Numero de elementos:",len(segunda_lista))

tercera_lista = list()
print(tercera_lista)
print("Numero de elementos:",len(tercera_lista))

cuarta_lista = []
print(cuarta_lista)
print("Numero de elementos:",len(cuarta_lista))

numero = 2
print(f"Elemento numero {numero} de la lista:{primera_lista[numero]}")
primera_lista[numero] = 15
print("Elemento numero", numero,"de la lista:",primera_lista[numero])
print(f"Elementos de la lista:{primera_lista[:4]}")

for elemento in primera_lista:
    elemento = elemento+1
    print(elemento)

lista_de_listas = [primera_lista,segunda_lista,tercera_lista,cuarta_lista]
print(lista_de_listas)
print(lista_de_listas[1][1])

quinta_lista = [50,5,176,233,46,8]

print(quinta_lista)
quinta_lista.sort()
print(quinta_lista)
quinta_lista.reverse()
quinta_lista.append(11)
print(quinta_lista)
quinta_lista.clear()
print(quinta_lista)

#Lista como pila
primera_pila = []

primera_pila.append(1)
primera_pila.append(13)
primera_pila.append(125)
print(primera_pila)
print(primera_pila.pop())
print(primera_pila)

#Lista como cola
primera_cola = []

primera_cola.append(6)
primera_cola.append(18)
primera_cola.append(4)
print(primera_cola)
print(primera_cola.remove(primera_cola[0]))
print(primera_cola)