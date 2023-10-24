# Una empresa desea calcular el sueldo total de una persona bajo los siguientes rubros: percepciones, sueldo base, 5% canasta básica,
# 3% prima antiguedad y deducciones. Si el salario base excede los $10,00 el ISR es del 30% y menos el 20%.Indique de cuánto es el
# total de la nómina a pagar y cuánto debe pagar de impuestos

from guizero import Text,TextBox,PushButton,App

suma = 0
impuesto = 0
def suma_nomina():
    global suma, impuesto
    salario = salario1.value
    if salario.isdigit():
        salario = int(salario1.value)
        if salario >= 10000:
            isr = .3 * salario
        else: 
            isr = .20 * salario
        canasta_basica = .05 * salario
        prima_antiguedad = 0.03 * salario
        suma += salario+canasta_basica+prima_antiguedad-isr
        impuesto += isr
        salario1.clear()
    else:
        app.info(title="Error",text="Sólo puedes ingresar números")
        salario1.clear()

def imprimir_nomina():
    message_nomina.value = f"La nómina a pagar es: {suma}"
    message_isr.value = f"Los impuestos a pagar son: {impuesto}"

app = App(title="Calcular nómina")
message = Text(app,text="Ingrese el salario del trabajador")
salario1 = TextBox(app)
button1 = PushButton(app, text="Siguiente salario",command=suma_nomina)
button2 = PushButton(app, text="Total",command=imprimir_nomina)
message_nomina = Text(app,text="")
message_isr = Text(app,text="")
app.display()
