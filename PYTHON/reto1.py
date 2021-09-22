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