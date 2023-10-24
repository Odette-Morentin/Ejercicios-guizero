# Obtenga la suma de 5 números entre 5 y 10 inclusive
from guizero import Text,TextBox,PushButton,App

contador = 0
suma_total = 0

def suma():
    global contador,suma_total
    num = numero.value
    if num.isdigit():
        num = int(numero.value)
        if num>=5 and num<=10:
            contador +=1
            suma_total += num
            numero.clear()
            if contador==5:
                button.hide()
                message_suma.value = f"El resultado es: {suma_total}"
        else:
            app.info(title="Error",text="Sólo puedes ingresar números entre 5 y 10")
    else:
        app.info(title="Error",text="Sólo puedes ingresar números")

app = App(title="Suma de números entre 5 y 10")
message = Text(app, text="Ingresa un número entre 5 y 10")
numero = TextBox(app)
button = PushButton(app, text="Siguiente número", command=suma)
message_suma = Text(app,text="")
app.display()
