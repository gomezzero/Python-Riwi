
# print('''Mercado riwi''')
# print(f'''     Opciones
#       [1]vas a comprar
#       [2]vas a devolver
#       [3]cerrar el programa
#       ''')
# mercado_riwi = input("vas a comprar?, vas a devolver").lower() 
# if (mercado_riwi == "comprar "):
#     print("que vas a comprar ")
# elif (mercado_riwi == "devolver "):
#     print("que vas a devolver? ")
# elif (mercado_riwi == " "):
#     print("opcion incorrecta")


usuario = input("inserata tu usuriao: ")
contraseña = str(input("insera tu contraseña: "))

if(usuario=="admin" and contraseña=="1234"):     
    print('''[1]vas a comprar [2]vas a devolver [3]cerrar el programa''')
    dinero=True
    opcion = int(input("ingrese la opcion: "))
    if(opcion==1 and dinero==True):
        print("vas a comprar")
    elif(opcion==2):
        print("vas a devolver")
    else:
        print("adios")
else:
        print("adios")




    
    
    


    
