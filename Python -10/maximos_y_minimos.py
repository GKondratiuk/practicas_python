cant_numeros = 4 
numero_maximo = 0


for cont in range (cant_numeros):
    print("ingrese un numero", cont +1)
    num = int(input())

    if num > numero_maximo:
        numero_maximo = num

print(f"El numero maximo es {numero_maximo} ")