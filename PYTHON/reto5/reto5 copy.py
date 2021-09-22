import csv

archivo = open('data.csv', mode='r', encoding='utf-8-sig')
info = csv.reader(archivo)

pacientes = []
promedio = 0 
alerta = ""
datos = [] 

for i in info:
    cliente = []
    if "nombre_completo" not in i:
        promedio = (float(i[4]) + float(i[5]) + float(i[6]) + float(i[7])) / 4
    
        cliente.append(i[0])
        cliente.append(i[1])
        cliente.append(i[2])
        cliente.append(i[3])
        cliente.append(promedio)

        if i[1] == "F" and promedio < 13.2:
            alerta = "Baja"
        elif i[1] == "F" and (promedio >= 13.2 and promedio <= 16.6):
            alerta = "Normal"
        elif i[1] == "F" and promedio > 16.6:
            alerta = "Alta"
        elif i[1] == "M" and promedio < 11.6:
            alerta = "Baja"
        elif i[1] == "M" and (promedio >= 11.6 and promedio <= 15):
            alerta = "Normal"
        elif i[1] == "M" and promedio > 15:
            alerta = "Alta"
        
        cliente.append(alerta)
        
        pacientes.append(cliente)
        datos.append(i[1])
        datos.append(i[3])       


sede =  int(input('***Ingresa la sede a consultar***'))
hemoglobina = float(input('***Ingresa la Hemoglobina a consultar***'))

indicea = 0 
indiceb = 0
p_alto = 0 
p_bajo = 99.9
c_punt_mayor = 0 
c_punt_menor = 0
c_punt_igual = 0

for j in range(len(pacientes)):
    if int(pacientes[j][3]) == sede:
        if pacientes[j][4] > p_alto:
            p_alto = pacientes[j][4]
            indicea = j
        if pacientes[j][4] < p_bajo:
            p_bajo = pacientes[j][4]
            indiceb = j 

for j in range(len(pacientes)):
        if pacientes[j][4] > hemoglobina:
            c_punt_mayor += 1
        if pacientes[j][4] < hemoglobina:
            c_punt_menor += 1
        if pacientes[j][4] == hemoglobina:
            c_punt_igual += 1      
        
print(f"{pacientes[indicea][0]} {pacientes[indicea][1]} {pacientes[indicea][2]} {pacientes[indicea][5]}")       
print(f"{pacientes[indiceb][0]} {pacientes[indiceb][1]} {pacientes[indiceb][2]} {pacientes[indiceb][5]}")
print(c_punt_mayor, c_punt_menor, c_punt_igual)
print(f"M {datos.count('M')}")
print(f"F {datos.count('F')}") 
print(f"1 {datos.count('1')}")  
print(f"2 {datos.count('2')}")      
print(f"3 {datos.count('3')}")  
print(f"4 {datos.count('4')}")      
print(f"5 {datos.count('5')}")  
print(f"6 {datos.count('6')}")      
print(f"7 {datos.count('7')}")  
print(f"8 {datos.count('8')}")      
print(f"9 {datos.count('9')}")  
print(f"10 {datos.count('10')}")      
print(f"11 {datos.count('11')}")  
print(f"12 {datos.count('12')}")      
print(f"13 {datos.count('13')}")  
print(f"14 {datos.count('14')}")      
print(f"15 {datos.count('15')}")  