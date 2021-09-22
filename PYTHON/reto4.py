num_pacientes=int(input())
c_hombres=0
c_mujeres=0
pacientes=[]

for i in range(num_pacientes):
    datos=input().split(' ')
    genero=int(datos[0])
    promedio=0
    datos_vec=[]
    datos_vec.append(genero)

    for j in range(1,8):
        promedio+=float(datos[j])

    promedio=promedio/7

    datos_vec.append(promedio)

    if genero==1:  
        c_mujeres+=1
    elif genero==2:
        c_hombres+=1
    
    def alerta(promedio,genero):
        if genero==1:
            if promedio<13.2:
                return 'Baja'
            elif promedio>=13.2 and promedio<=16.6:
                return 'Normal'
            elif promedio>16.6:
                return 'Alta'
        if genero==2: #Masculino
            if promedio<11.6:
                return 'Baja'
            elif promedio>=11.6 and promedio<=15:
                return 'Normal'
            elif promedio>15:
                return 'Alta'
    datos_vec.append(alerta(promedio,genero))
    pacientes.append(datos_vec)

ind_alto=0
ind_bajo=0
pro_alto=0
pro_bajo=99.9

for i in range(len(pacientes)):
    if pacientes[i][1] > pro_alto:
        pro_alto=pacientes[i][1]
        ind_alto=i
    if pacientes[i][1] < pro_bajo:
        pro_bajo=pacientes[i][1]
        ind_bajo=i
    
print(f"{pacientes[ind_alto][0]} {pacientes[ind_alto][1]:.2f} {pacientes[ind_alto][2]}")
print(f"{pacientes[ind_bajo][0]} {pacientes[ind_bajo][1]:.2f} {pacientes[ind_bajo][2]} ")
print(c_hombres, c_mujeres)


