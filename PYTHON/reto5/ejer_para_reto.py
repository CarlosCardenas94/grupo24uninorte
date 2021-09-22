#Genero     Categoria     Puntaje
#F Fem      No Aprobado   0-2      
#F Fem      Aprobado      3-5
#M Masc     No Aprobado   0-3
#M Masc     Aprobado      4-5

import csv

archivo = open('data.csv', mode='r', encoding='utf-8-sig')
info = csv.reader(archivo)

estudiantes = []
promedio = 0 
alerta = ""
datos = [] 

for i in info:
    alumno = []
    if "nombre_completo" not in i:
        promedio = (float(i[4]) + float(i[5]) + float(i[6]) + float(i[7])) / 4
    
        alumno.append(i[0])
        alumno.append(i[1])
        alumno.append(i[2])
        alumno.append(i[3])
        alumno.append(promedio)

        if i[1] == "F" and promedio < 3:
            alerta = "No aprobado"
        elif i[1] == "F" and (promedio >= 3 and promedio <= 5):
            alerta = "Aprobado"
        elif i[1] == "M" and promedio < 4:
            alerta = "No aprobado"
        elif i[1] == "M" and (promedio >= 4 and promedio <= 5):
            alerta = "Aprobado"
        
        alumno.append(alerta)
        
        estudiantes.append(alumno)
        datos.append(i[1])
        datos.append(i[3])       

print(estudiantes)
sede = int(input())
puntaje = float(input())

indicea = 0 
indiceb = 0
p_alto = 0 
p_bajo = 99.9
c_punt_mayor = 0 
c_punt_menor = 0
c_punt_igual = 0

for j in range(len(estudiantes)):
    if int(estudiantes[j][3]) == sede:
        if estudiantes[j][4] > p_alto:
            p_alto = estudiantes[j][4]
            indicea = j
        if estudiantes[j][4] < p_bajo:
            p_bajo = estudiantes[j][4]
            indiceb = j
        if estudiantes[j][4] > puntaje:
            c_punt_mayor += 1
        if estudiantes[j][4] < puntaje:
            c_punt_menor += 1
        if estudiantes[j][4] == puntaje:
            c_punt_igual += 1      
        

print(f"{estudiantes[indicea][0]} {estudiantes[indicea][1]} {estudiantes[indicea][2]} {estudiantes[indicea][5]}")       
print(f"{estudiantes[indiceb][0]} {estudiantes[indiceb][1]} {estudiantes[indiceb][2]} {estudiantes[indiceb][5]}")
print(c_punt_mayor, c_punt_menor, c_punt_igual)
print(f"M {datos.count('M')}")
print(f"F {datos.count('F')}") 
print(f"1 {datos.count('1')}")  
print(f"2 {datos.count('2')}")      



