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
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener un dato utilizando el Dialog Prompt
y luego mostrarlo utilizando el Dialog Alert

La empresa spaceX , nos contrata para poder hacer el cálculo de precio final y descuentos para un viaje al espacio exterior
el costo por millón de kilómetros es de 8 bitcoin 

podes viajar a Marte (60 millones de KM) , la Luna (½ millón de KM)y a Titan (1300 millones de KM)
podes elegir si viajar en verano, primavera  otoño o invierno.

para los viajes a Marte
Si viajan más de 5 personas te hacemos un 50 % de descuento sobre el precio,
viajando en verano al precio con descuento se le suma un 10% , en otoño y primavera se le suma un 25% al precio con descuento.

para los viajes la Luna 
si viajan más de 5 personas te hacemos un 40 % de descuento sobre el precio,
viajando en verano al precio con descuento se le suma un 15% ,  en otoño y primavera al precio con descuento se le suma un 25%

para los viajes a Titan
si viajan más de 5 personas te hacemos un 30 % de descuento sobre el precio,
viajando en verano al precio final se le suma un 10% , en otoño y primavera al precio con descuento se le suma un 20%

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):

        pasajeros = prompt("", "cuantos viajan")
        pasajeros = int(pasajeros)

        lugar = prompt("", "Ingrese destino: marte, luna, titan")
        estacion = prompt("", "ingrese estacion del año Invierno, primavera, otoño, verano")

        costo = 8
        descuento = 0
        descuento_extra = 0


        if lugar == "marte":
            km = 60
            if pasajeros > 5:
                descuento = 50
                if estacion == "verano":
                    descuento_extra = 10
                elif estacion != "invierno":
                    descuento_extra = 25
        
        elif lugar == "luna":
            km = 0.5
            if pasajeros > 5:
                descuento = 40
                if estacion == "verano":
                    descuento_extra = 15
                elif estacion != "invierno":
                    descuento_extra = 25
        
        elif lugar == "titan":
            km = 1300
            if pasajeros > 5:
                descuento = 30
                if estacion == "verano":
                    descuento_extra = 10
                elif estacion != "invierno":
                    descuento_extra = 20
        
        precio = costo * km
        ahorro = precio * descuento / 100
        precio_con_descuento = precio - ahorro

        ahorro_extra = precio_con_descuento * descuento_extra / 100
        precio_con_descuento_extra = precio_con_descuento - ahorro_extra


        
        
        mensaje= f"son {pasajeros} pasajeros \n con destino a {lugar} \n vale {precio} bitcoins \n tienen un descuento de {descuento} % \n valor {precio_con_descuento}\n descuento extra {descuento_extra} % \n total {precio_con_descuento_extra}"

        alert("",mensaje)





        


    
        







               

       
        
       
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()