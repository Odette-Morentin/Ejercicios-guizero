# suma de todos los cuadrados de los números pares entre o y 20 consecutivos
from guizero import App,Text,TextBox,PushButton

app = App(title="Suma de los cuadrados de los pares del 0 al 20")

def calcular_cuadrados():
    c = 0
    suma = 0
    while c<=20:
        suma = suma+(c**2)
        c = c+2
    message_suma.value = f"La suma es: {suma}"

message = Text(app,text="suma de los cuadrados de los números pares entre o y 20 consecutivos")
Button = PushButton(app,text="Calcular",command=calcular_cuadrados)
message_suma = Text(app,text="")

app.display()
