#Cuadrado de un número positivo leído del tacldo
from guizero import App, PushButton, Text, TextBox

app = App(title="Cuadrado de un número positivo")

def calcular_cuadrado():
    num = numero.value
    if num.isdigit():
        num = int(numero.value)
        message_cuadrado.value = f"El cuadrado de {num} es: {num**2}"
    else:   
        app.info(title="Error", text="Sólo puedes ingresar números positivos")

message = Text(app,text="Ingresa un número positivo")
numero = TextBox(app)
button = PushButton(app, text="Calcular cuadrado",command=calcular_cuadrado)
message_cuadrado = Text(app,text="")

app.display()
