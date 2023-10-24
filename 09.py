# Capture n enteros positivos, obtenga la suma del cuadrado de los pares y el cubo de los impares
from guizero import App,Text,TextBox,PushButton

suma = 0
def sumar_numeros():
    global suma
    num = numero.value
    if num.isdigit():
        num = int(numero.value)
        if num % 2 == 0:
            suma += num**2
        else:
            suma +=num**3
    else:
        app.info(title="Error",text="Sólo puedes ingresar números positivos")
    numero.clear()

def imprimir_suma():
    message_suma.value = f"El resultado es: {suma}"



app = App(title="Suma de cuadros y cubos")

message = Text(app,text="Ingresa un número positivo")
numero = TextBox(app)
button1 = PushButton(app,text="Ingresar número",command=sumar_numeros)
button2 = PushButton(app,text="Calcular suma",command=imprimir_suma)
message_suma = Text(app,text="")

app.display()
