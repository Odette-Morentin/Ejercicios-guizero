#Promedio de 3 números
from guizero import App, Text, TextBox, PushButton

def promedio():
    num1 = num_1.value
    num2 = num_2.value
    num3 = num_3.value

    if num1.isdigit() and num2.isdigit() and num3.isdigit():
        num1 = int(num_1.value)
        num2 = int(num_2.value)
        num3 = int (num_3.value)
        prom:float = (num1+num2+num3)/3
        message_promedio.value = f"El promedio es: {prom}"
    else:
        app.info(title="Error",text="Solo puedes ingresar números")
       
  
app = App(title="Promedio de 3 números")

message = Text(app,text="Dame un número",)
num_1 = TextBox(app)
message = Text(app,text="Dame un número",)
num_2 = TextBox(app)
message = Text(app,text="Dame un número",)
num_3 = TextBox(app)

button = PushButton(app, text="Promedio", command= promedio)
message_promedio = Text(app, text="")

app.display()
