import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Guillermo   
apellido: Kondratiuk
---
Ejercicio: entrada_salida_02
---
En el parque de diversiones "Aventuras Extremas", un grupo de 10 amigos ha 
decidido disfrutar del día probando las diferentes atracciones y luego se reúnen en un
restaurante para compartir un delicioso almuerzo. Antes de que llegue la cuenta, deciden 
crear un programa para calcular y dividir los gastos de manera equitativa. 
Se pide ingresar los siguientes datos hasta que el usuario lo desee:

Para cada amigo (pedir por prompt)

Nombre del amigo, #NO NO NO NO SE VALIDA (NO HACE FALTA)
Plato principal elegido ("Pizza", "Hamburguesa", "Ensalada").  
Cantidad de platos principales pedidos (debe ser al menos 2).

Bebida elegida ("Refresco", "Agua", "Jugo").
Cantidad de bebidas pedidas (debe ser al menos 2).


Se conocen los siguientes precios base:

El precio unitario de cada plato principal es de $3000.

El precio unitario de cada bebida es de $1000.


Una vez ingresados todos los datos, el programa debe calcular e informar lo siguiente (informar por print):

Informar cual fue el tipo de bebida más vendida.
Los porcentajes de cada tipo de platos pedidos (teniendo en cuenta su cantidad). Ejemplo: [30% pizza, 40% ensaladas,
30% hamburguesas]
Informar la cantidad total de bebidas que fueron “Refresco”.
El promedio gastado en platos principales de tipo “Pizza” sobre el grupo de amigos en general.
El nombre de la persona que pidió la menor cantidad de platos principales de tipo “Hamburguesa”

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        
        continuar = True
        amigos = 0

        valor_plato = 3000
        valor_bebida = 1000

        cantidad_platos = 0
        cantidad_bebidas = 0

        agua = 0
        jugo = 0
        refresco = 0

        pizza = 0
        hamburguesa = 0
        ensalada = 0        

        while(continuar):
            
            nombre = prompt("Nombre", "Ingrese su nombre")

            plato = prompt("P.Principal","'pizza', 'hamburguesa', 'ensalada'")
            while(plato != "pizza" and plato != "hamburguesa" and plato != "ensalada" ):
                plato = prompt("P.Principal","Debe ser 'pizza', 'hamburguesa', 'ensalada'")

            cantidad_platos = prompt("Platos", "Cuantos platos va a pedir ?")
            cantidad_platos = int(cantidad_platos)
            while(cantidad_platos < 2):
                cantidad_platos = prompt("Platos", "Cuantos platos va a pedir ? tienen que ser al menos 2")

            
            bebida = prompt("Bebida","'refresco', 'agua', 'jugo'")
            while(bebida != "refesco" and bebida != "agua" and bebida != "jugo" ):
                bebida = prompt("Bebida","Re ingrese'refresco', 'agua', 'jugo'")

            cantidad_bebidas = prompt("Bebidas", "Cuantas bebidas va a pedir ?")
            cantidad_bebidas = int(cantidad_bebidas)
            while(cantidad_bebidas < 2):
                cantidad_bebidas = prompt("Bebidas", "Cuantas bebidas va a pedir ? deben ser al menos 2")
                cantidad_bebidas = int(cantidad_bebidas)

            amigos = amigos + 1

            
            match bebida:
                case "agua":
                    agua = agua + cantidad_bebidas
                case "jugo":
                    jugo = jugo + cantidad_bebidas
                case _:
                    refresco = refresco + cantidad_bebidas

            bandera_hamburguesa = True
            bandera_pizza = True
            match plato:
                case "pizza":
                    bandera_pizza = False
                    pizza = pizza + 1
                    valor_plato = valor_plato * cantidad_platos
                case "ensalada":
                    ensalada = ensalada + 1
                case _:
                    hamburguesa = hamburguesa + 1
                    bandera_hamburguesa = False
                    if bandera_hamburguesa == False:
                        
                        nombre_menor_hamburguesa = nombre
                    

            if agua > jugo and agua > refresco:
                bebida_preferida = "Agua fue la mas pedida"
            elif jugo > agua:
                bebida_preferida = "Juego fue el mas pedido"
            else:
                bebida_preferida = "Refresco"

            
            
            continuar = prompt("Pedido","Desean seguir pidiendo S/N?")
            if continuar == "s":
                continuar = True
            else:
                continuar = False

        if bandera_pizza == False:
            promedio_gastado = valor_plato / amigos
        else:
            promedio_gastado = "No pidieron pizza"

        porcentaje_pizza = (pizza * 100) / amigos
        porcentaje_hamburguesa = (hamburguesa * 100) / amigos
        porcentaje_ensaldada = (ensalada * 100) / amigos
        
        print(f"plato {plato}")
        print(f"bebida {bebida}")
        print(f"cantidad de bebidas {cantidad_bebidas}")
        print(f"cantidad de platos {cantidad_platos}")
        print(f"la bebida mas tomada es {bebida_preferida}")
        print(f"El porcentaje de pizza es {porcentaje_pizza} \n hamburguesa {porcentaje_hamburguesa} \n ensalada {porcentaje_ensaldada}")
        print(f"La cantidad de refresco fue {refresco}")
        print(f"El promedio gastado en pizzas fue de {promedio_gastado}")
        print(f"el que pidió menor cantidad de hamburguesas fue {nombre_menor_hamburguesa}")
        
       
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()