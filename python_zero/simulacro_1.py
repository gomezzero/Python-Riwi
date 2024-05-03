
# variables necesarias
nombre = input("porfavor ingras tu nombre: ")
peso = float(input("porfavor ingras tu peso: "))
astatura = float(input("porfavor ingras tu estatura: "))

# formula de calculo IMC
formula = (peso/(astatura*astatura))
print(formula)

# posibles respuestas
if formula<18.5:
    print(nombre,"tienes bajo peso")
elif formula>18.5 and formula<24.9:
    print(nombre,"tienes un peso normal")
elif formula>25 and formula<29.9:
    print(nombre,"tienes sobrepeso")
elif formula>30 and formula<34.9:
    print(nombre,"tienes obesidad tipo I")
elif formula>35 and formula<39.9:
    print(nombre,"tienes obesidad tipo II")
elif formula>40 and formula<49.9:
    print(nombre,"tienes obesidad tipo III")
elif formula>=50:
    print(nombre,"tienes obesidad tipo I")




