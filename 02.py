#Calcular la edad de una persona preguntando el año actual, el año de nacimiento y validando que el año actual sea mayor que el de nacimiento y
#validar que el año actual sea mayor a 0

from guizero import Text,App,PushButton,TextBox

def calcular_edad():
    a_actual = an_actual.value
    a_nacimiento = an_nacimiento.value

    if a_actual.isdigit() and a_nacimiento.isdigit():
        a_actual = int(an_actual.value)
        a_nacimiento = int(an_nacimiento.value)
        if a_actual<=0 or a_actual<a_nacimiento:
            app.info(title="Error",text="El año actual debe de ser mayor a 0 y mayor al año de nacimiento")
        else:
            message_edad.value = (f"Tu edad es: {a_actual-a_nacimiento}")
    else:
        app.info(title="Error",text="Solo puedes ingresar números")
    
    


app = App(title="Calcular edad")

message = Text(app,text="Ingresa el año actual")
an_actual = TextBox(app)
message = Text(app,text="Ingresa tu año de nacimiento")
an_nacimiento = TextBox(app)
buttom = PushButton(app,text="Calcular edad",command=calcular_edad)
message_edad = Text(app,text="")

app.display()
