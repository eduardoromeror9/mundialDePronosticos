from prettytable import PrettyTable

legend = """
  🔥🔥 INFORMACION IMPORTANTE 🔥🔥
  Don Eduardo Romero,
  mejor conocido como 
  el KING de los PRONOSTICOS
  ES EL VIGENTE CAMPEON
         HASTA QUE 
  SE DEMUESTRE LO CONTRARIO
  \n"""

jornadas = """  
        Jornadas: 23
        Juegos: 69
"""

info = """
"""

title = PrettyTable(['🔥🔥 Mundial de pronosticos 🔥🔥'])
tabla_dia = PrettyTable(['Players', 'G-P', 'DIF', 'PCT %'])
tabla_dia.add_row([' #######',   '43-26', '-', ' 620 ']) 
tabla_dia.add_row([' Erycherd',  '42-27', '1', ' 610 '])
tabla_dia.add_row([' Eduardo',   '41-28', '2', ' 595 '])
tabla_dia.add_row([' Christian', '41-28', '2', ' 595 '])
tabla_dia.add_row([' Steven',    '40-29', '3', ' 580 '])
tabla_dia.add_row([' Daniel',    '40-29', '3', ' 580 '])
tabla_dia.add_row([' Kleydi',    '39-30', '4', ' 565 '])



print('\n',jornadas)
# print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)