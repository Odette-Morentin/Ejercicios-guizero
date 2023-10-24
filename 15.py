# La tienda "Brankos" debe vender productos a n alumnos, ofrecen tortas, tacos, hotdogs y pizza. Imprime los productos vendidos en total

from guizero import Text,App,TextBox, Combo,PushButton

tortas = 0
tacos = 0
hotdogs = 0
pizza = 0

def seleccionar_producto():
    global tortas,tacos,hotdogs,pizza
    seleccion = seleccion1.value
    cantidad = cantidad1.value
    if cantidad.isdigit():
        cantidad = int(cantidad1.value)
        cantidad1.clear()
        match seleccion:
            case "Tortas":
                tortas += cantidad
            case "Tacos":
                tacos += cantidad
            case "Hotdogs":
                hotdogs += cantidad
            case "Pizza":
                pizza += cantidad
        if tortas+tacos+hotdogs+pizza >=2:
            button3.show()
    else:
        app.info(title="Error",text="Sólo puedes ingresar números positivos")

def total():
    message_total.value = f"El total de productos vendidos fueron: {tortas+tacos+pizza+hotdogs}\n Tortas vendidas: {tortas}\n Tacos vendidos: {tacos}\n Hotdogs vendidos: {hotdogs}\n Pizzas vendidas: {pizza}"





app = App(title="Brankos")

message = Text(app,text="Selecciona el producto a comprar",size="13")
seleccion1 = Combo(app,options=["Tortas","Tacos", "Hotdogs", "Pizza"])
message = Text(app, text="¿Cuántos?",size="13")
cantidad1 = TextBox(app)
button1 = PushButton(app,text="Agregar producto",command=seleccionar_producto)
button3 = PushButton(app, text="Sacar total",command=total)
button3.hide()
message_total = Text(app,text="")


app.display()
