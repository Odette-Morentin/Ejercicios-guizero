# Genere la siguiente serie: 01

from guizero import App,Text,PushButton

def generar_serie():
    for i in range(10):
        message_serie.value += "01"
    

app = App()
button = PushButton(app,text="Generar rango",command=generar_serie)
message_serie = Text(app,text="",color="green",size="25")

app.display()
