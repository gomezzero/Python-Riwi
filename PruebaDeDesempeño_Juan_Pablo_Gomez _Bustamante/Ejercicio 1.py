
cantidad = []

carrito = []

productos = [
    {
        "nombre" : "camisa negra",
        "valor" : 12000,
    },
    {
        "nombre" : "camisa azul",
        "valor" : 11000,
    },
    {
        "nombre" : "camisa verde",
        "valor" : 13000,
    }  
]
while True:
    menu = int(input("""
            menu de acciones
             
             1) ver productos
             2) ver tabla de descuentos 
             3) agragar a carrito de compras 
             4) ver carrito de compras
             5) ver monto a pagar
             6) apagar
             
             Que accion quieres realizar: """))

    
    if menu == 1:
        posicion = 0
        for i in productos :
            print(f""" id:{posicion} {i["nombre"]} y su valor es: {i["valor"]}.""")

            posicion+= 1
        
    elif menu == 2:
        
        print("""   estos son los posibles descuentos a los qu epuedes aplicar:
              
            • Si compras entre 5 y 10 artículos optienes descuento del 5%.
            • Si compras entre 11 y 20 artículos optienes un descuento del 10%.
            • Si compras más de 20 artículos, optienes un descuento del 15%.
              """)
    elif menu == 3:
            
        producto_buscar = int(input("que producto quieres agregar a tu carrito?, escibe su id: "))
            
        print(f"""que cantidad de {productos[producto_buscar]["nombre"]}quieres agregar""")
        
        cantidad_elejir = int(input(": "))
        
        #carrito producto es una variable creada para falicitar futuras operaciones
        carrito_producto = []
        carrito_producto.append(productos[producto_buscar]["nombre"])
        carrito_producto.append(productos[producto_buscar]["valor"])
        carrito_producto.append(cantidad_elejir)
        carrito_producto.append(productos[producto_buscar]["valor"] * cantidad_elejir)
        carrito.append(carrito_producto)
        cantidad.append(cantidad_elejir)
        
                
    elif menu == 4:
        
        print(carrito)
            
    #descuentos  
    elif menu == 5:
        
        suma_cantidad = 0
        
        for i in carrito:
            
            suma_cantidad += i[2]
            
            precio_pagar_neto = i[1] * suma_cantidad
        
        if suma_cantidad >= 5 and suma_cantidad <= 10:
            
            cantidad_pagar = (precio_pagar_neto-(precio_pagar_neto * 0.05))
            
            deacuento = precio_pagar_neto * 0.05
            
            print(f"""el monto total es de: {precio_pagar_neto}""")
            print(f"""felicitaciones tienes un descuento de {deacuento}, el valor a pagar es: {cantidad_pagar}""")
            
        elif suma_cantidad >= 11 and suma_cantidad == 20:
            
            cantidad_pagar = (precio_pagar_neto-(precio_pagar_neto * 0.10))
            
            deacuento = precio_pagar_neto * 0.10
            
            print(f"""el monto total es de: {precio_pagar_neto}""")
            print(f"""felicitaciones tienes un descuento de {deacuento}, el valor a pagar es: {cantidad_pagar}""")
            
        elif suma_cantidad > 20 :
            
            cantidad_pagar = (precio_pagar_neto-(precio_pagar_neto * 0.15))
            
            deacuento = precio_pagar_neto * 0.15
            
            print(f"""el monto total es de: {precio_pagar_neto}""")
            print(f"""felicitaciones tienes un descuento de {deacuento}, el valor a pagar es: {cantidad_pagar}""")


            
    elif menu == 6:
        
        break
            
            
        
                