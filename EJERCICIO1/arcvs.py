from Pais import *
import csv
listaPais=[]
with open('C:\\pais.csv',encoding='utf-8') as csvPaisFile:

    csvReader=csv.reader(csvPaisFile)    
    for row in csvReader:
        ob=Pais(row[0],row[1],row[2],row[3])
        listaPais.append(ob)


for apr in listaPais:

    print('nombre:',apr.getNombre())
    print('altura :',apr.getaltura())
    print('poblacion:',apr.getpoblacion())
    print('eda_me:',apr.geteda_me())