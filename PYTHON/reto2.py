hombre_baja=0
hombre_alta=0
hombre_normal=0
mujer_baja=0
mujer_alta=0
mujer_normal=0
var_gen=0
num_pacientes=int(input())
for i in range(num_pacientes):
  var_hemo=float(input())
  var_gen=int(input())
  while var_gen != 1 and var_gen!= 2: 
    var_gen=int(input())
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
print(hombre_baja,hombre_alta,hombre_normal,mujer_baja,mujer_alta,mujer_normal,end=(" "))