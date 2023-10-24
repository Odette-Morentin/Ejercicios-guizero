# dado el año de nacimiento indique cuántos años va a cumplir una persona el siguiente año
from guizero import Text,TextBox,PushButton,App

a_actual= 2023
def calcular_edad():
    global a_actual
    an_nacimiento = a_nacimiento.value
    if an_nacimiento.isdigit():
        an_nacimiento = int(a_nacimiento.value)
        if an_nacimiento>2023:
            app.info(title="Error",text="El año debe ser menor o igual a 2023")
        else:
            message_edad.value = f"El siguiente año tendrás: {(a_actual-an_nacimiento)+1} años"
    else:
        app.info(title="Error",text="Sólo puedes ingresar números postivos")

app = App(title="Edad el siguiente año")
message = Text(app,text="Ingresa tu año de nacimiento")
a_nacimiento = TextBox(app)
button1 = PushButton(app,text="Calcular edad", command=calcular_edad)
message_edad = Text(app,text="")

app.display()
