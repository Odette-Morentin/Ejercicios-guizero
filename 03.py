# Promedio de m números del teclado positivos

from guizero import App,Text,TextBox,PushButton

suma = 0
lista_num = []

def ingresar_números():
    global suma
    num = numeros.value
    if num.isdigit():
        num = int(numeros.value)
        lista_num.append(num)
        suma = suma + num
        numeros.clear()
        if len(lista_num)>=2:
            button2.show()
    else:
        app.info(title="Error",text="Solo puedes ingresar números positivos")

def promediar():
    message_promedio.value = f"El promedio es:{suma/len(lista_num)}"


app = App(title="Promedio de m números")

message = Text(app,text="Ingresar al menos dos números para promediar")
numeros = TextBox(app)
button1 = PushButton(app,text="Siguiente número", command=ingresar_números)
button2 = PushButton(app,text="Promediar",command=promediar)
button2.hide()
message_promedio = Text(app,text="")

app.display()
