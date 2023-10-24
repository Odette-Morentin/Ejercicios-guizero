# Obtener la edad promedio de n personas preguntándole su año de nacimiento y suponiendo que el año actual es 2023

from guizero import Text,TextBox,PushButton,App

lista = []
suma = 0

def ingresar_anios():
    global suma
    a_nacimiento = anios.value
    if a_nacimiento.isdigit():
        a_nacimiento = int(anios.value)
        if a_nacimiento==0:
            app.info(title="Error",text="El año de nacimiento debe ser mayor a 0")
        elif a_nacimiento>2023:
            app.info(title="Error",text="El año de nacimiento debe ser menor o igual a 2023")
        else:
            lista.append(a_nacimiento)
            suma += (2023 - a_nacimiento)
            anios.clear()
        if len(lista)>=2:
            button2.show()
    else:
        app.info(title="Error",text="Sólo puedes ingresar números")

def promedio():
    message_promedio.value = (f"El promedio de edad es: {suma/len(lista)}")


app = App(title="Edad promedio de n personas preguntando su año de nacimiento")
message = Text(app,text="Ingresa un   año de nacimiento")
anios = TextBox(app)
button1 = PushButton(app,text="Ingresar año",command=ingresar_anios)
button2 = PushButton(app, text="Calcular promedio",command=promedio)
button2.hide()
message_promedio = Text(app,text="")

app.display()
