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
          Jornadas: 26
          Juegos: 78
"""

info = """
       Christian debe 1
"""

title = PrettyTable(['🔥🔥 Mundial de pronosticos 🔥🔥'])
tabla_dia = PrettyTable(['Players', 'G-P', 'DIF', 'PCT %'])

tabla_dia.add_row([' Eduardo',   '47-31', '-', ' 605 '])
tabla_dia.add_row([' Kleydi',    '45-33', '2', ' 575 '])
tabla_dia.add_row([' Erycherd',  '45-33', '2', ' 575 '])
tabla_dia.add_row([' Christian', '45-32', '2', ' 575 '])
tabla_dia.add_row([' CarlosJ',   '45-33', '2', ' 575 '])
tabla_dia.add_row([' Steven',    '43-35', '4', ' 550 '])
tabla_dia.add_row([' Daniel',    '43-35', '4', ' 550 '])


print('\n',jornadas)
print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)