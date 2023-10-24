# Se desea saber la cantidad de alumnos que pasaron una materia, son 25 y la calificación aprobatoria es 7

from guizero import App,Text,TextBox,PushButton

alumnos = 25
aprobados = 0
calificaciones_ingresadas = 0

def alumnos_aprobados():
    global alumnos, aprobados,calificaciones_ingresadas
    cal = calificaciones.value
    if cal.isdigit():
        cal = int(calificaciones.value)
        if cal>10:
            app.info(title="Error",text="Ingresa una calificación entre 0 y 10")
            calificaciones.clear()
        else:
            calificaciones_ingresadas += 1
            calificaciones.clear()
            if cal>=7:
                aprobados += 1
            if calificaciones_ingresadas==alumnos:
                message_alumnos.value=f"Aprobaron: {aprobados} alumnos"
                button1.hide()  
    else:
        app.info(title="Error",text="Solo puedes ingresar números positivos")


app = App(title="Cantidad de alumnos que pasaron")

message = Text(app,text="Ingresa las calificaciones")
calificaciones = TextBox(app)
button1 = PushButton(app,text="Siguiente calificación",command=alumnos_aprobados)
message_alumnos = Text(app,text="")

app.display()
