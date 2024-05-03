inventario_cafe = [
   {
        'nombre' : 'cafe corriente',
        'cantidad' :10,
        'precio' : 15000,
        'categoria':"cafe carriente"
    },
    {
        'nombre' : 'cafe especial',
        'cantidad' : 9,
        'precio' : '25000',  
        'categoria':"cafe especial"      
    },
     {
        'nombre' : 'cafe premium',
        'cantidad' : '5',
        'precio' : '35000',
        'categoria':"cafe premium"
    }
]

while True:

    lista_de_accion = int(input('''que accion deceas realizar?
                            
                    1. Agregar un nuevo producto al inventario.
                    2. Actualizar la cantidad de un producto existente en el inventario.
                    3. Eliminar un producto del inventario.
                    4. Listar todos los productos en el inventario.
                    5. Verificar si un producto específico está en el inventario.
                                                                                '''))
    if lista_de_accion == 1:
        nombre_nueva_categoria = input("ingrasa el nombre de la nueva categoria: ")
        inventario_cafe[nombre_nueva_categoria]={}

        nombre_producto_nuevo = input("que nombre le vas a dar a este producto: ")
        cantidad_nueva_categoria = int(input("que cantidad tienes del nuevo producto: "))
        precio_nueva_categoria = int(input("cual es el valor del nuevo producto:"))

        inventario_cafe[nombre_nueva_categoria]['nombre'] = nombre_producto_nuevo
        inventario_cafe[nombre_nueva_categoria]['cantidad'] = cantidad_nueva_categoria
        inventario_cafe[nombre_nueva_categoria]['precio'] = precio_nueva_categoria
        print("guardado")
    elif lista_de_accion == 2:
        for i in inventario_cafe:
            print(f'''productos: {i}''')
        productos_a_modificar = input("que producto quieres modificar: ")
        if productos_a_modificar in inventario_cafe:
            accion_de_modificaion = int(input('''
                    1. vas a eliminar
                    2. vas a agregar
                                    '''))
            if accion_de_modificaion == 1:
                cantidda_nueva = int(input("cauntos articulos vas a eliminar?: "))
                inventario_cafe[productos_a_modificar]["cantidad"] -=  cantidda_nueva
                print("guardado")
                print(inventario_cafe)
            elif accion_de_modificaion == 2:
                cantidda_nueva = int(input("caunto articulos quieres agregar?: "))
                inventario_cafe[productos_a_modificar]["cantidad"] += cantidda_nueva
                print("guardado")
                print(inventario_cafe)
            else: 
                print("error en opciones")
        else:
            print("producto incexistente")
    elif lista_de_accion == 3:
        for i in inventario_cafe:
            print(f'''producto: {i}''')
        producto_a_eliminar = input("que producto quieres eliminar: ")
        if producto_a_eliminar in inventario_cafe:
            del inventario_cafe[producto_a_eliminar]
            print("guardado")
            print(inventario_cafe)
        else:
            print("el producto no fue encontrado")
    elif lista_de_accion == 4:
        for cafe in  inventario_cafe:
            print(f"""
                  nombre=> {cafe['nombre']}
                  cantidad=> {cafe['cantidad']}
                  precio=> {cafe['precio']}
                  """)

