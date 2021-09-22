
num_pacientes=int(input())

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
        datos=input().split(' ')
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

print(f"{prom_phombres:.2f} {alerta(prom_phombres, 2)}")
print(f"{prom_pmujeres:.2f} {alerta(prom_pmujeres, 1)}")
print(hombres_sup,mujeres_sup)
print(hombres_bajo,mujeres_bajo)
print(hombres_igual,mujeres_igual)







