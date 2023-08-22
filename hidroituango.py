nivelAngua = int (input("Ingrese el nivel del agua: "))

# evaluando multiples condiciones

if (nivelAngua > 0 and nivelAngua <= 200):
    print(f"el nivel de agua es: {nivelAngua}, esta bajo")
elif(nivelAngua > 200 and nivelAngua <= 400):  
     print(f"el nivel de agua es: {nivelAngua}, esta normal")
elif(nivelAngua > 400 ):  
     print(f"el nivel de agua es: {nivelAngua}, esta alto, inicie evacuacion")
else:
    print(f"por favor revise el nivel del agua")