#operadores aritméticos
a = 15
b = 8
#suma
print("Suma:")
c = a+b
print(c)
#resta
print("Resta:")
c = b-a 
print(c)

#producto
print("Producto:")
c = a*b
print(c)

#división
print("División:")
c = a/b
print(c)

#módulo
print("Módulo:")
c = a%b
print(c)

#potencia
print("Potencia:")
c = a**b
print(c)

#Realiza la división con resultado de número entero
print("División con resultado entero:")
c = a//b
print(c)

#operadores a nivel de bits
a = 3
b = 5
c = 4
#AND
print("AND:")
d = a&b 
print(d)
d = c&b 
print(d)
#OR
print("OR:")
d = a|b 
print(d)
d = c|b 
print(d)
#XOR
print("XOR:")
d = a ^ b 
print(d)
d = c ^ b 
print(d)
#NOT
e = 25
f = False
print("NOT:")
g = ~e
print(g)
g = ~f 
print(g)

#Corrimiento izquierda
print("Corrimiento izquierda:")
a = 5 << 2
print(a)

#Corrimiento derecha
print("Corrimiento derecha:")
a = 5 >> 2
print(a)


#operadores de comparación

#igual que
print("igual que")
result = a == b
print(result)

#diferente de
print("diferente de")
result = a != b
print(result)
#mayor qué
print("mayor qué")
result = a > b
print(result)
#menor qué
print("menor qué")
result = a < b
print(result)
#mayor o igual qué
print("mayor o igual qué")
result = a >= b
print(result)
#menor o igual qué
print("menor o igual qué")
result = a <= b
print(result)

#Operadores de comparación booleana 

#AND 
print("AND comparación:")
print((True and True))

#OR 
print("OR comparación:")
print((False or True))

#negado 
print("Comparación negada:")
print(not True)