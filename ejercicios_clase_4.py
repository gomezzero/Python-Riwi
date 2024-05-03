lista = []


agraagdos = {f'''{lista.append (input("agraga numeros : "))},
            {lista.append (input("agraga numeros : "))},
            {lista.append (input("agraga numeros : "))},
            {lista.append (input("agraga numeros : "))},
            {lista.append (input("agraga numeros : "))},
            {lista.append (input("agraga numeros : "))},
            {lista.append (input("agraga numeros : "))}'''}
print(lista)

# vercion con siclo for

# for NumeroContador in range(1,6):
#    numero = int(input("agraga numeros : "))
#    lista.append(numero)
# print(lista)

# vercion while
# numero_de_vueltas= 1

# while numero_de_vueltas!=6:
#     numero = int(input(f'''agraga numeros: {numero_de_vueltas}: '''))
#     lista.append(numero)
#     numero_de_vueltas+=1
#     # print(f''' {numero_de_vueltas}''')

# ejercicio 1

# listaEstudianteRiwi = []

# ingres_otro_estudiante = "si"
# while ingres_otro_estudiante == "si":

#     nombre = input("ingresa tu nombre: ")
#     correo = input("ingresa tu correo: ").upper()
#     edad = int(input("ingresa tu edad: "))
#     apellido = input("ingresa tu apelllido: ")
#     direccion = input("ingresa tu direccion: ")

#     estudiantes = {
#         "nombre" : nombre,
#         "correo" : correo,
#         "edad" : edad,
#         "apellido" : apellido,
#         "direccion" : direccion
#     }
#     listaEstudianteRiwi.append(estudiantes)
#     respuesta =input("ingresa si quieres ingresar a otro estudiante?: ")
#     if respuesta!= "si":
#         ingres_otro_estudiante = False
        
# print(listaEstudianteRiwi)
        
# # *****************************************************

# for estudiante in listaEstudianteRiwi:
#     print(f"""
#           {estudiante["nombre"].upper()},
#           {estudiante["apellido"].capitalize()},
#           {estudiante["correo"].lower()},
#           {estudiante["edad"]}, 
#           {estudiante["direccion"].title()}
#     """)

# # *********************************

# coders = [
#     {
#         "nombre":input("ingresa tu nombre: "),
#         "apellido":input("ingresa tu apelllido: "),
#         "direccion":input("ingresa tu direccion: "),
#         "edad":int(input("ingresa tu edad: "))
        
#     },
#     {
#         "nombre":input("ingresa tu nombre: "),
#         "apellido":input("ingresa tu apelllido: "),
#         "direccion":input("ingresa tu direccion: "),
#         "edad":int(input("ingresa tu edad: "))
#     }
# ]
# for i in coders:
#     print(i["nombre"])
