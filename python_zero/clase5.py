productos = (
    
    {
    "nombre" : "pan",
    "valor" : 1000
    }, 
    {        
    "nombre" : "galleta",
    "valor" : 1000
    },
    {
        "nombre" : "arina",
        "valor" : 1500  
    }    
)

documento_cliente = ""
nombre_cliente = ""
apellido_cliente = ""
factura = []
        
while  True:
    print("MENU")

    menu = '''  
            1) Registrar cliente.
            2) Registrar un nuevo producto a la factura.
            3) Listar productos actuales de la factura.
            4) Mostrar factura.
            5) Apagar el programa.
    '''

    print(menu)

    opcion_menu = input("INGRESE LA OPCION: ")

    if opcion_menu == "1":
        
        if(documento_cliente == "" or nombre_cliente == "" or apellido_cliente == ""):    
            print("vamos a registrarte")  
            
            documento_cliente = input("ingresa tu documento: ")
            nombre_cliente = input("ingresa tu nombre: ")
            apellido_cliente = input("ingresa tu apellido: ")
            print("documento: ", documento_cliente)
            print("nombre: ", nombre_cliente)
            print("apellido; ", apellido_cliente)    
          
        else:
            print("ya tenemos a un cliente registrado")
            print("documento: ", documento_cliente)
            print("nombre: ", nombre_cliente)
            print("apellido; ", apellido_cliente) 
            respuesta = input("vas a reescribir los datos)1 para si  para no 2 ")   
            
            if respuesta == "1":
                documento_cliente = input("ingresa tu documento: ")
                nombre_cliente = input("ingresa tu nombre: ")
                apellido_cliente = input("ingresa tu apellido: ")
                print("documento: ", documento_cliente)
                print("nombre: ", nombre_cliente)
                print("apellido; ", apellido_cliente)
            
            else:   
                print("opcion invalida")                         
#############################################################          
    elif opcion_menu == "2":
        indice = 0
        for producto in productos:
            print(f'''[{indice}] {producto["nombre"]} {producto["valor"]}''')
            indice += 1
        producto = int(input("ingrese el indice del producto a agragar: "))
        factura.append(productos[producto])    
    elif opcion_menu == "3":
        print(f'''[{indice}] {producto["nombre"]} {producto["valor"]}''')
        print("factura actual")
#############################################################           
    elif opcion_menu == "4":      
        print(factura)
        print("documento: ", documento_cliente)
        print("nombre: ", nombre_cliente)
        print("apellido; ", apellido_cliente) 
        
#############################################################     
    elif opcion_menu == "5":
        print("Apagando el sistema...")
        print("###########################")
        break
#############################################################     
    else:
        print("###########################")
        print("opcion invalida")
        print("###########################")

####################descuentos#################################    
    
for i in factura:
    if i["nombre"]== "pan":
        print("tienes un pan")

# print(factura[1]["valor"])
