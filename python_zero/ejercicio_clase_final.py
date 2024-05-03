print("veterinaria Dalí ")

pacientes = []

while True:
    menu = print(f"""
                
                1. Registrar paciente 
                2. Actualizar paciente (Se deben poder actualizar todos los campos) 
                3. Ver pacientes activos (Que están en la veterinaria) 
                4. Ver pacientes Inactivos (Que no están en la veterinaria o fueron dados de alta) 
                5. Salir del programa. 
                
                """)
    menu_desicion = int(input("que haccion quieres realizar: "))
    if menu_desicion == 1:
        
        nombre = input("ingrese el nombre del nuevo paciente: ")
        edad = int(input("ingrese la edad: "))
        raza = input("ingrese la raza: ")
        identificación_dueño = input("ingrese la identificación del dueño: ")
        estado_del_paciente = input("ingrese si es paciente esta activo: ")
        
        paciente_nuevo ={
                    "nombre" : nombre,
                    "edad" : edad,
                    "raza" : raza,
                    "identificación_dueño" : identificación_dueño,
                    "estado_del_paciente" : estado_del_paciente,
        }             
        pacientes.append(paciente_nuevo)
        
    # elif menu_desicion == 2:
    #     repetidor = 0
    #     for i in paciente_nuevo:
    #         print(f""" pacientes actuales
    #               pocicion:{repetidor}  nombre:{i["nombre"]}""")
    #         repetidor += 1
    #         modificar = input("de que paciente quiere modificar un campo: ") 

    #         for i in paciente_nuevo: 
    #             print(f"""pacientes activos nombre: {i["nombre"]} 
    #                   edad: {i["edad"]} 
    #                   raza: {i["raza"]} 
    #                   identificacion del cueño: {i["identificación_dueño"]} 
    #                   estado del paciente: {i["estado_del_paciente"]}
    #                   """)
                
    #             modificar_categoria = input("de que paciente quiere modificar una categoria: ") 
                
    #             del paciente_nuevo[modificar_categoria]
    #             nombre = input("ingrese el nuevo nombre dek paciente: ")
    #             edad = int(input("ingrese la edad: "))
    #             raza = input("ingrese la raza: ")
    #             identificación_dueño = input("ingrese la identificación del dueño: ")
    #             estado_del_paciente = input("ingrese si es paciente esta activo: ")
        
                 
                 
    elif menu_desicion == 3:  
        
        for i in pacientes:
            
            if i["estado_del_paciente"] == 'si' :
                print(f""" pacientes activos nombre: {i["nombre"]} 
                      edad: {i["edad"]} 
                      raza: {i["raza"]} 
                      identificacion del cueño: {i["identificación_dueño"]} 
                      estado del paciente: {i["estado_del_paciente"]}
                      """)
    elif menu_desicion == 4:
        
        for i in pacientes:
            
            if i["estado_del_paciente"] != 'si' :
                print(f""" pacientes activos nombre: {i["nombre"]} 
                      edad: {i["edad"]} 
                      raza: {i["raza"]} 
                      identificacion del cueño: {i["identificación_dueño"]} 
                      estado del paciente: {i["estado_del_paciente"]}
                      """)
    elif menu_desicion == 5:
        
        break

        
