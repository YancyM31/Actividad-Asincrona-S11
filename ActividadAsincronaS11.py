# Obtener del usuario la cantidad de numeros a ingresar
while True:
    try:
        dato = int(input("Ingrese la cantidad de números a evaluar: "))
        if dato <= 0:
            print("Ingrese un número que sea mayor a cero")
            continue
        break
    except ValueError:
        print("Ingrese un número válido")

# Determinar las variables para poder contar los numeros
Positivos = 0
Negativos = 0
Nulos = 0

i = 1

# Obtener los números y clasificarlos segun su tipo
for i in range(dato):
    while True:
        try:
            num = int(input(f"Ingrese el número {i+1}: "))
            break
        except ValueError:
            print("Ingrese un número válido")
    if num > 0:
        Positivos += 1
    elif num < 0:
        Negativos += 1
    else:
        Nulos += 1

# Mostrar los resultados segun lo ingresado por el usuario
print("La cantidad de números positivos es: ", Positivos)
print("La cantidad de números negativos es: ", Negativos)
print("La cantidad de números nulos es: ", Nulos)

print("Fin del progama")






























