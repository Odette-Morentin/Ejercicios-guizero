# menú de una calculadora funcional que pueda sumar, restar, multiplicar y dividir seleccionando el tipo de operacion. Dar 2 números.

from guizero import Text,Combo,TextBox,App,PushButton

def operaciones():
    num1 = numero1.value
    num2 = numero2.value
    operacion = operacion_aritmetica.value
    if num1.isalpha() or num2.isalpha():
        app.info(title="Error",text="Sólo puedes ingresar números")
    else:
        num1 = float(numero1.value)
        num2 = float(numero2.value)
        match operacion:
            case "Suma":
                message_resultado.value = f"La suma es: {num1+num2}"
            case "Resta":
                message_resultado.value = f"La resta es: {num1-num2}"
            case "Multiplicación":
                message_resultado.value = f"La multiplicación es: {num1*num2}"
            case "División":
                message_resultado.value = f"La división es: {num1/num2}"

app = App(title="Calculadora")

message = Text(app,text="Ingresa dos números")
numero1 = TextBox(app)
numero2 = TextBox(app)
message = Text(app, text="Selecciona la operación que desees realizar")
operacion_aritmetica = Combo(app,options=["Suma","Resta","Multiplicación","División"])
button = PushButton(app,text="Realizar operación", command=operaciones)
message_resultado = Text(app,text="")

app.display()
