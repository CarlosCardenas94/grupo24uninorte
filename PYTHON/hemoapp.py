def reto1():
    var_hemo=float(input("Ingresa tu medicion de Hemoglobina: "))
    var_gen=int(input("Ingresa tu genero(1:Femenino o 2:Masculino): "))
    if var_hemo<13.2 and var_gen==1 or var_hemo<11.6 and var_gen==2:
        print("Baja")
    elif var_hemo>13.2 and var_hemo<16.6 and var_gen==1 or var_hemo>11.6 and var_hemo<=15 and var_gen==2:
        print("Normal")
    elif var_hemo>16.6 and var_gen==1 or var_hemo>15 and var_gen==2:
        print("Alta")
    else:
        print("No es posible generar la alerta")

def reto2():
    hombre_baja=0
    hombre_alta=0
    hombre_normal=0
    mujer_baja=0
    mujer_alta=0
    mujer_normal=0
    var_gen=0
    num_pacientes=int(input('Ingrese el numero de pacientes a estudiar: '))
    for i in range(num_pacientes):
        var_hemo=float(input('Ingrese el valor de Hemoglobina: '))
        var_gen=int(input('Ingrese su genero Femenino(1) Masculino(2): '))
        while var_gen != 1 and var_gen!= 2: 
            var_gen=int(input('Ingrese su genero Femenino(1) Masculino(2): '))
        if var_hemo<13.2 and var_gen==1:
            mujer_baja+=1
        elif  var_hemo<11.6 and var_gen==2:
            hombre_baja+=1
        elif var_hemo>13.2 and var_hemo<16.6 and var_gen==1: 
            mujer_normal+=1
        elif var_hemo>11.6 and var_hemo<=15 and var_gen==2:
            hombre_normal+=1
        elif var_hemo>16.6 and var_gen==1:
            mujer_alta+=1
        elif var_hemo>15 and var_gen==2:
            hombre_alta+=1
    print('\n***RESULTADOS***')
    print(f'Hombres con hemoglobina Baja:{hombre_baja}')
    print(f'Hombres con hemoglobina Alta:{hombre_alta}')
    print(f'Hombres con hemoglobina Normal:{hombre_normal}')
    print(f'Mujeres con hemoglobina Baja:{mujer_baja}')
    print(f'Mujeres con hemoglobina Alta:{mujer_alta}')
    print(f'Mujeres con hemoglobina Normal:{mujer_normal}')

def reto3():
    num_pacientes=int(input('Ingrese el numero de pacientes a estudiar: '))

    hemo_mujeres=[] 
    hemo_hombres=[]
    hombres_sup=0
    hombres_bajo=0
    hombres_igual=0
    mujeres_sup=0
    mujeres_bajo=0
    mujeres_igual=0


    for i in range(num_pacientes):
        var_gen=0
        while var_gen!=1 and var_gen!=2:
            datos=input('Ingrese hemoglobina y genero en una linea (Separe con espacio): ').split(' ')
            hemoglobina=float(datos[0])
            var_gen=int(datos[1])

            if var_gen==2:
                hemo_hombres.append(hemoglobina)
            elif var_gen==1:
                hemo_mujeres.append(hemoglobina)

    if len(hemo_hombres)==0:
        prom_phombres=0
    else:
        prom_phombres=sum(hemo_hombres)/len(hemo_hombres)

    if len(hemo_mujeres)==0:
        prom_pmujeres=0
    else:
        prom_pmujeres=sum(hemo_mujeres)/len(hemo_mujeres)


    def alerta(promedio,genero):
        if genero==1:
            if promedio<13.2:
                return'Baja'
            elif promedio>=13.2 and promedio<=16.6:
                return'Normal'
            elif promedio>16.6:
                return'Alta'
        elif genero==2:
            if promedio<11.6:
                return'Baja'
            elif promedio>=11.6 and promedio<=15:
                return'Normal'
            elif promedio>15:
                return'Alta'

    for ph in hemo_hombres:
        if ph > prom_phombres:
            hombres_sup+=1
        elif ph < prom_phombres:
            hombres_bajo+=1
        else:
            hombres_igual+=1

    for ph in hemo_mujeres:
        if ph > prom_pmujeres:
            mujeres_sup+=1
        elif ph < prom_pmujeres:
            mujeres_bajo+=1
        else:
            mujeres_igual+=1
    print('\n***RESULTADOS***')
    print(f"Hemoglobina promedio Hombres: {prom_phombres:.2f} {alerta(prom_phombres, 2)}")
    print(f"Hemoglobina promedio Mujeres: {prom_pmujeres:.2f} {alerta(prom_pmujeres, 1)}")
    print(f'Hombres arriba del promedio: {hombres_sup}')
    print(f'Hombres abajo del promedio: {hombres_bajo}')
    print(f'Hombres igual al promedio: {hombres_igual}')
    print(f'Mujeres arriba del promedio: {mujeres_sup}')
    print(f'Mujeres abajo del promedio: {mujeres_bajo}')
    print(f'Mujeres igual al promedio: {mujeres_igual}')

def reto4():
    num_pacientes=int(input('Ingrese el numero de pacientes a estudiar: '))
    c_hombres=0
    c_mujeres=0
    pacientes=[]

    for i in range(num_pacientes):
        datos=input('Ingrese hemoglobina y genero en una linea (Separe con espacio): ').split(' ')
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
        
    print(f"\nPaciente con el promedio más alto {pacientes[ind_alto][0]} {pacientes[ind_alto][1]:.2f} {pacientes[ind_alto][2]}")
    print(f"Paciente con el promedio más más {pacientes[ind_bajo][0]} {pacientes[ind_bajo][1]:.2f} {pacientes[ind_bajo][2]} ")
    print(f'Hombres en el estudio: {c_hombres} \nMujeres en el estudio: {c_mujeres}')

def reto5():
    print('En proceso')

op=0

def menu(op):
        if op==1:
            reto1()
        elif op==2:
            reto2()
        elif op==3:
            reto3()
        elif op==4:
            reto4()
        elif op==5:
            reto5()
        elif op==6:
            print("Has salido del sistema")
        else:
            print("Elige una opción valida")

while op !=6:
        print("\n***BIENVENIDO***")
        op=int(input("Elige una opción:\n 1.Estudiar el nivel de hemoglobina de un paciente\n 2.Estudiar la hemoglobina en varios pacientes y saber su alerta\n 3.Analizar el promedio y alerta de un grupo de pacientes\n 4.Analizar el promedio y alerta de un grupo de pacientes en un periodo de una semana\n 5.reto5\n 6.Salir\n"))
        menu(op)