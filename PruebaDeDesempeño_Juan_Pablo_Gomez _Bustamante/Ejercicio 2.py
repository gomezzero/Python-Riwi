print("biblioteca")

# libors disponibles en la biblioteca
libros = [
    
    {
        "nombre": "el libro de las sombras",
        "disponible": "no"
    },
    {
        "nombre": "el libro de la luz",
        "disponible": "si"
    },
    {
        "nombre": "el libro de la noche",
        "disponible": "no"
    },
    {
        "nombre": "el libro maldito de zeref",
        "disponible": "si"
    }    
]
# usuarios de la bioblioteca
usuarios = [
    
    {  
        "nombre": "pepe",
        "membresia" : "si"
    },
    {  
        "nombre": "daniel",
        "membresia" : "no"
    },
    {  
        "nombre": "natsu",
        "membresia" : "si"
    },
    {  
        "nombre": "zeref",
        "membresia" : "no"
    }
]
#cilo para el prestamo de libors
while True:
    menu = int(input(""" menu de acciones
                 1) ver usuarios
                 2) prestamo de libros
                 """))
#muestra usuarios   
    if menu == 1:
        contador = 0
        for i in usuarios:
            print(f""" id: {contador} 
    usuario: {i["nombre"]}""")
            
            contador += 1 
            
    elif menu == 2:
        usuario_prestamo = int(input("""porfavor ingrese el id de tu usuario: """))
 #alamcena el id del usuario en una variable para su busqueda  
        usuario_busqueda = usuarios[usuario_prestamo]
        
#los siguientes if y elif son para confirmar menbrecias  
        if usuario_busqueda["membresia"] == "si" :
                print("tu menbrecia esta activa puedes prestar un libro")
                contador = 0
                #este siclo for es para el prestamo de libros   
                for i in libros: 
                    print(f""" id: {contador} libro: {i["nombre"]}""")
                    contador += 1      
                                           
                liblo_prestar = int(input("""porfavor ingrese el id del libro:"""))
                libro_busqueda = libros[liblo_prestar]
                
                if libro_busqueda["disponible"] == "si":
                        print("tu libro esta disponible puedes llevartelo")
                        break  
                                      
                elif libro_busqueda["disponible"] == "no":
                    print("lo sentimos mucho, tu libro no esta disponible")
                    break 
                                           
        elif usuario_busqueda["membresia"] == "no" : 
            print("tu menbrecia no esta activa no puedes prestar un libro")
            break
    else:
        print("opcion incorrecta")
