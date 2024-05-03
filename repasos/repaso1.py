print("BIENBENIDO A TIENDA RIWI")

usuarios = []


identificacion = int (input("ingresa tu numero de identificacion: "))
nombre = input("ingresa ti nombre: ")
apellidos = input("ingresa tus apellidos: ")

papa = 10000
arepa =  5000
manzana = 3000

usuario = {
    "identificacion":identificacion,
    "nombre":nombre,
    "apellidos":apellidos
}

usuarios.append(usuario)

print("menu de acciones")


 
accion = int(input(f'''
             que deseas hacer?
            1. agregar un producto a tu carrito
            2. ver lista de productos
            3.ver factura
            4.salir
'''))

if accion == 1 :
   print(f'''los productos: 
        {manzana}
        {arepa}
        {papa}
            {input("eleji un producto: ")} ''')
          
else:
   print(productos)
   

# productos = []

# papa = 19.000
# manzana = 2.000
# cargador = 6.000


# print("MENU ACCIONES")

