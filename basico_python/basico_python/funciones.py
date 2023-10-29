def Suma(num1,num2):
    resultado = num1+num2
    return resultado

def division_exacta(num1,num2):
    division = num1//num2
    modulo = num1%num2
    return division,modulo

def primera_funcion():
    print("Hola mundo, esta es mi primera funcion")
    return

def segunda_funcion(name = "Daniel"):
    print(f"Hola, mi nombre es {name}")
    return

primera_funcion()
val1 = 20
val2 = 7

print("Suma total:",Suma(5,6))
division,modulo=division_exacta(val1,val2)
print(f"El resultado de dividir {val1} entre {val2} es: {division} y sobran {modulo}")

segunda_funcion("Monica")
