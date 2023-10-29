
print("for")
for i in range(5):
    print(i)

for i in range(15,20):
    print(i)

#Cómo harías una cuenta regresiva?

print("while")
j = 0
while j<10:
    print(j)
    j+=1

listaDeElementos = {"Alma","Brenda","Camila"}
for elemento in listaDeElementos:
    print(elemento)

print("Ingrese la contraseña:")
password = input()
while("pedro" != password):
    print("Contraseña incorrecta, intente de nuevo")
    password = input()
print("Contraseña correcta!")

#cuenta regresiva
print("Cuenta regresiva con ciclo while")
counter = 10
while 0<counter:
    print(counter-1)
    counter-=1

print("Cuenta regresiva con ciclo for")
limite = 10
for i in range(limite):
    print(limite - i-1)