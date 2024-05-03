personas = {
    "llave1":{
        "nombre"  :"zeref", 
        "edad" : 320,
        "ciudad" : "mildiand"
    },
    "llave2" : {
        "nombre"  :"natsu", 
        "edad" : 320,
        "ciudad" : "mildiand"

        }
}

# personas["profecion"] = input("agrege profecion: ") 

for i in personas:

    personas[i]["profecion"] = input("agrege profecion: ") 

print(personas)


# # personas["llave1"]["profecion"] = input("que profecion quieres darle: ")
# # for i, detalles in personas.items():
# #     for iterador in detalles:
# #         print(iterador)

# decicion = input("quieres var algo de los diccionarios: ")
# if decicion == "si":
#     cual_de_dos = int(input("""quieres ver el primero (1) el segundo (2) o ambos (3): 
#                             """))
# if decicion == "si" and cual_de_dos == 1:
#         # for
#         decicion2 = int(input(f"""que quieres ver 1(nombre) 2 (edad) 3(ciudad) 4(profecion): 
#                             """))
#         if decicion2 ==1:
#             print(personas["llave1"]["nombre"])

#         elif decicion2 ==2:
#             print(personas["llave1"]["edad"])
#         elif decicion2 == 3 :
#             print(personas["llave1"]["ciudad"])
#         elif decicion2== 4:
#             print(personas["llave1"]["profecion"])
#         else:
#             print("incorrecto")
# elif decicion == "si" and cual_de_dos == 2:

#         decicion2 = int(input(f"""que quieres ver 1(nombre) 2 (edad) 3(ciudad) 4(profecion): 
# #                             """))
# #         if decicion2 ==1:
# #             print(personas["llave2"]["nombre"])
# #         elif decicion2 ==2:
# #             print(personas["llave2"]["edad"])
# #         elif decicion2 == 3 :
# #             print(personas["llave2"]["ciudad"])
# #         elif decicion2== 4:
# #             print(personas["llave2"]["profecion"])
# #         else:
# #             print("incorrecto")

# # elif decicion == "si" and cual_de_dos == 3:

# #         decicion2 = int(input(f"""que quieres ver 1(nombre) 2 (edad) 3(ciudad) 4(profecion): 
# #                             """))
# #         if decicion2 ==1:
# #             print(personas["llave2"]["nombre"])
# #             print(personas["llave1"]["nombre"])
# #         elif decicion2 ==2:
# #             print(personas["llave2"]["edad"])
# #             print(personas["llave1"]["edad"])
# #         elif decicion2 == 3 :
# #             print(personas["llave2"]["ciudad"])
# #             print(personas["llave1"]["ciudad"])
#         elif decicion2== 4:
#             print(personas["llave2"]["profecion"])
#             print(personas["llave1"]["profecion"])
#         else:
#             print("incorrecto")
# else:
#     print("okay adios")



# #####################################################################################################################
    
# libro = {
#         "libro1":{
#             "titulo" : "la guerra de los cielos",
#             "autor" : "fulanito",
#             "año de publicacion" : 2015,
#         }
# }

# print(libro)

# informacion = libro|personas
# print(informacion)
# personas["llave1"]["nombre"] = "zac"
# print(personas)