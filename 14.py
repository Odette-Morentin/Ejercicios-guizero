# Determinar qué día de la semana es dado un número
from guizero import Text,PushButton,App, TextBox

def obtener_dia():
    dia_sem = dia_semana.value
    if dia_sem.isdigit():
        dia_sem = int(dia_semana.value)
        if 1 <= dia_sem <= 7:
             dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
             message_dia.value = f"El día de la semana es: {dias[dia_sem-1]}"
        else:
            app.info(title="Error",text="Número fuera de rango")
    else:
        app.info(title="Error",text="Sólo puedes ingresar números positivos")


app = App(title="Día de la semana")

message = Text(app,text="Ingresa un número entre 1-7")
dia_semana = TextBox(app)
button = PushButton(app, text="Obtener día",command=obtener_dia)
message_dia = Text(app,text="")

app.display()
