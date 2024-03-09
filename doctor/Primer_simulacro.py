import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

""" 
Simulacro 01 - Dr. UTN

Nombre:
Apellido:

Enunciado:

De 5 personas que ingresan al hospital se deben tomar y validar los siguientes datos.
    ● Nombre 
    ● Temperatura, entre 35 y 42
    ● Sexo( f, m , nb )
    ● Edad(mayor a 0)

Pedir datos por Prompt y mostrar por Print

Punto A - por el número de DNI del alumno:

DNI terminados en 0 o 1

1) Informar la cantidad de personas de sexo femenino
2) La edad promedio de personas de sexo masculino
3) El nombre de la persona la persona de sexo nb con más temperatura(si la hay)

DNI terminados en 2 o 3
1) Informar la cantidad de personas de sexo masculino
2) La edad promedio de personas de sexo nb
3) El nombre de la persona de sexo femenino con la temperatura mas baja(si la hay)

DNI terminados en 4 o 5
1) Informar la cantidad de personas de sexo nb
2) La edad promedio de personas de sexo femenino
3) El nombre de la persona la persona de sexo masculino con la temperatura mas baja(si la hay)

DNI terminados en 6 o 7
1) Informar la cantidad de personas mayores de edad (desde los 18 años)
2) La edad promedio en total de todas las personas mayores de edad (18 años)
3) El nombre de la persona la persona de sexo masculino con la temperatura mas baja(si la hay)

DNI terminados en 8 o 9
1) Informar la cantidad de personas menores de edad (menos de 18 años)
2) La temperatura promedio en total de todas las personas menores de edad
3) El nombre de la persona de sexo femenino con la temperatura mas baja(si la hay)

Todos los alumnos:
B - Informar cual fue el sexo mas ingresado
C - El porcentaje de personas con fiebre y el porcentaje sin fiebre




  personas = 0
        temperatura_total = 0
        es_menor = 0
        temperatura_mas_baja = float ('inf')
        mujer_temperatura_mas_baja = None
        con_fiebre = 0
        sin_fiebre = 0
        es_femenino = float ('inf')
        es_masculino = float ('inf')
        es_nobinario = float ('inf')

        while(personas < 5):
            nombre = prompt("Nombre","Escriba su nombre")
            
            
            temperatura = prompt("temperatura", "Ingrese su temperatura")
            temperatura = int(temperatura)
            
            while(temperatura < 35 or temperatura > 42):
                temperatura = prompt("temperatura", "Re-Ingrese su temperatura")
                temperatura = int(temperatura)
            
            sexo = prompt("Genero", "Indique su genero 'f','m', 'nb'")
            while(sexo != "f" and sexo != "m" and sexo != "nb"):
                  sexo = prompt("Genero", "Indique nuevamente su genero 'f','m', 'nb'")
            
            edad = prompt("Edad", "Indique su edad")
            edad = int(edad)
            while(edad < 0):
                edad = prompt("Edad", "Indique su edad")
                edad = int(edad)

            if edad < 18:
                es_menor = es_menor  + 1 
                temperatura_total = temperatura_total + temperatura
            personas = personas + 1

            if sexo == "f" and temperatura < temperatura_mas_baja:
                temperatura_mas_baja = temperatura
                mujer_temperatura_mas_baja = nombre



            if sexo == "m":
                es_masculino = es_masculino + 1
            elif sexo == "f":
                es_femenino = es_femenino + 1
            else: 
                es_nobinario = es_nobinario + 1
            
            

        if es_masculino > es_femenino and es_masculino > es_nobinario:
            sexo_predominante = "masculino"
        elif es_femenino > es_nobinario:
            sexo_predominante = "femenino"
        else:
           sexo_predominante = "no binario"


        if temperatura > 37:
            con_fiebre = con_fiebre + 1 
        elif temperatura < 37:
            sin_fiebre = sin_fiebre + 1

        porcentaje_con_fiebre = con_fiebre / personas * 100
        porcentaje_sin_fiebre = sin_fiebre / personas * 100

        promedio = temperatura_total / es_menor



        alert("Informe", f"Cantidad de pacientes: {personas} \n Menores = {es_menor} \n promedio temperatura menores {promedio} \n paciente femenino con temperatura mas baja {mujer_temperatura_mas_baja} \n sexo mas ingresado {sexo_predominante} \n porcentaje con fiebre {porcentaje_con_fiebre} \n porcentaje sin fiebre {porcentaje_sin_fiebre}")
"""
