def conversor (dias,horas,minutos,segundos):
    totalmilise= (dias*86400000)+(horas*3600000)+(minutos*60000)+(segundos*1000)
    return totalmilise

dias=int(input("Ingresa la cantidad de dias: "))
horas= int(input("Ingresa la cantidad de horas: "))
minutos=int(input("Ingresa la cantidad de minutos: "))
segundos = int (input("Ingresa la cantidad de segundos: "))

valrototal=conversor(dias,horas,minutos,segundos)

print ("El valor total de los valores que proporcionaste es igual a: ",valrototal)
