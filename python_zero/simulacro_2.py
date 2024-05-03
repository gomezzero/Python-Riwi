numero_de_documento = ""
nombre = ""
apellido = ""

factura = []

factura_total = []

productos = [
    
    {
        "nombre" : "galletas",
        "precio" : 500,
        "categoria" : "parba"
    },
    
    {
        "nombre" : "pan",
        "precio" : 1000,
        "categoria" : "parba"
    },
    {
        "nombre" : "pan pizza",
        "precio" : 6000,
        "categoria" : "parba"
    },
    {
        "nombre" : "manzana",
        "precio" : 800,
        "categoria" : "fruta"
    },
    
    {
        "nombre" : "pera",
        "precio" : 1500,
        "categoria" : "fruta"
    },
    {
        "nombre" : "mango",
        "precio" : 6000,
        "categoria" : "fruta"
     },
    {
        "nombre" : "manzana caramelizada",
        "precio" : 8000,
        "categoria" : "dulce"
    },
    {
        "nombre" : "trufas de chocolate",
        "precio" : 5000,
        "categoria" : "dulce"
    },
    {
        "nombre" : "chocolate",
        "precio" : 3000,
        "categoria" : "dulce"
    },
    {
        "nombre" : "camioneta ford",
        "precio" : 300000000,
        "categoria" : "carros"
    }      
]
######################################################################333

# (1) Volver a registrar el documento, nombres y apellidos del cliente 
# (2) Agregar producto al carrito de compras – (Se debe agregar toda la información de los productos deseados por el usuario y adicional se debe agregar una cantidad, la cual es escogida por el usuario) 
# (3) Listar el carrito de compras, (deben mostrarse los productos que están en el carrito de compras, un valor subtotal y un valor total, el valor total contiene el IVA de la suma de todos los productos.). 
# Tenga en cuenta que se le debe aplicar IVA (19%) a toda la suma de las compras realizadas. Ejemplo: 
# si el valor total del carrito de compras tiene un valor total de 100.000 el valor que deberá pagar será 
# 119.000 
# (4) Actualizar carrito de compras (El usuario puede cambiar las cantidades de un producto en específico) 
# (5) Eliminar producto en carrito de compras 
# (6) Finalizar programa

print("MENU")

while True:
    menu = print(""" 
            1) Registrar nuevo cliente
            2) Agregar producto al carrito de compras
            3) Listar el carrito de compras
            4) Actualizar carrito de compras
            5) Eliminar producto en carrito de compras 
            6) Finalizar programa
    """)
    opciones_menu = int(input("ingrese una opcion: "))
    
    if opciones_menu == 1:
        if numero_de_documento == "" or nombre == "" or apellido == "":
            print("registrate")
            numero_de_documento = int(input("porfavor ingrese su numero de documento: "))
            nombre = input("porfavor ingrese su nombre: ") 
            apellido = input("porfavor ingrese sus aèllidos: ") 
            print("""hola {nombre} {apellido} tu numero de documento es {numero_de_documento}""")
        else:
            print("ya estas registrado")
            
    elif opciones_menu == 2:
        posicion = 0
        for i in productos :
            print(f""" {posicion} {i["nombre"]} y su valor es: {i["precio"]} ({i["categoria"]} )""")

            posicion+= 1
        producto_elejido = int(input("que producto quieres agregar a tu carrito?: "))
        
        cantidad = (f""" {posicion} {i["nombre"]} y su valor es: {i["precio"]} ({i["categoria"]} {i} )""")
        
        factura.append(productos[producto_elejido])   

        cantidad = int(input("que cantidad quieres agregar: ")) 
        
        productos.append(cantidad,["cantidad"])
        print(productos)
                
    elif opciones_menu == 3:
        factura_neta = 0
        for i in factura:

            print(f""" {i["nombre"]} y su valor es el siguiente: {i["precio"]} ({i["categoria"]})""")
            
        factura_neta += i["precio"]
        print("valor neto", factura_neta)
        
        factura_con_iva = (((factura_neta*cantidad)*0.19)+factura_neta)
        factura_total.append(factura_con_iva)
        print("valor con iva", factura_con_iva)
        
    elif opciones_menu == 4:   
            posicion = 0  
            for i in factura:
          
                    print(f""" {posicion}tienes este producto en tu carrito: {i["nombre"]} y su valor es: {i["precio"]} ({i["categoria"]} {i["cantidad"]})""")
                    posicion += 1
                    
            actualizar_carrito1 = int(input("que deceas eliminar del carrito de compras: "))
                    
            del factura[actualizar_carrito1]
            print("guardodo")
            siguiente = input("quieres borrar algun otro producto: ")
        
            if siguiente == "si":
                    
                posicion = 0  
                for i in factura:
                        print(f""" {posicion}tienes este producto en tu carrito: {i["nombre"]} y su valor es: {i["precio"]} ({i["categoria"]})""")
                posicion += 1
                    
                actualizar_carrito1 = int(input("que deceas eliminar del carrito de compras: "))
                    
                del factura[actualizar_carrito1]
                print("guardodo")
                siguiente = input("quieres borrar algun otro producto: ")
                    
            elif siguiente != "si":
                   print("adios")
    elif opciones_menu == 5:
        
        posicion = 0  
        for i in factura:
          
            print(f""" {posicion}tienes este producto en tu carrito: {i["nombre"]} y su valor es: {i["precio"]} ({i["categoria"]})""")
            posicion += 1
            
        actualizar_carrito = int(input("que deceas eliminar del carrito de compras: "))
            
        del factura[actualizar_carrito]
        print("guardodo")
        siguiente = input("quieres borrar algun otro producto: ")
   
        if siguiente == "si":
            
            posicion = 0  
            for i in factura:
                print(f""" {posicion}tienes este producto en tu carrito: {i["nombre"]} y su valor es: {i["precio"]} ({i["categoria"]})""")
            posicion += 1
            
            actualizar_carrito = int(input("que deceas eliminar del carrito de compras: "))
            
            del factura[actualizar_carrito]
            print("guardodo")
            siguiente = input("quieres borrar algun otro producto: ")
            
        elif siguiente != "si":
            print("adios")
            
    elif opciones_menu == 6:
        finalizacion = input("quieres terminar tus compras? ")
        if finalizacion == "si":
            print(f"""esto es el vaor a pagar {factura_total}""")
            break
            # pago = int(input("ingresa el numero de tu tarjeta de credito: "))
            # if pago == int:
            #     break