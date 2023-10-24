#Obtenga la suma de todos los cuadrados de n números capturados del teclado

from guizero import App,Text,PushButton,TextBox


lista = []
suma = 0

def suma_cuadrados():
    global suma
    num = numeros.value
    if num.isdigit():
        num = int(numeros.value)
        lista.append(num)
        suma += num**2
        numeros.clear()
        if len(lista) >=2:
            button2.show()
    else:
        app.info(title="Error",text="Sólo puedes ingresar números")

def imprimir_sumacuadrados():
    message_cuadrado.value = f"La suma del cuadrado es: {suma}"



app = App(title="Suma de cuadrados de n números")
message = Text(app,text="Ingresa los números a sumar")
numeros = TextBox(app)
button1 = PushButton(app,text="Siguiente número",command=suma_cuadrados)
button2 = PushButton(app,text="Calcular",command=imprimir_sumacuadrados)
button2.hide()
message_cuadrado = Text(app,text="")

app.display()
