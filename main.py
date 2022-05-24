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
          Jornadas: 28
          Juegos: 84
"""

info = """
  🧊🧊 Kleydi a la NEVERA 🧊🧊
"""

title = PrettyTable(['🔥🔥 Mundial de pronosticos 🔥🔥'])
tabla_dia = PrettyTable(['Players', 'G-P', 'DIF', 'PCT %'])

tabla_dia.add_row([' Eduardo',   '51-33', '-', ' 605 '])
tabla_dia.add_row([' Kleydi',    '50-34', '1', ' 595 '])
tabla_dia.add_row([' Erycherd',  '48-36', '3', ' 570 '])
tabla_dia.add_row([' Christian', '47-37', '4', ' 560 '])
tabla_dia.add_row([' CarlosJ',   '47-37', '4', ' 560 '])
tabla_dia.add_row([' Steven',    '45-39', '6', ' 535 '])
tabla_dia.add_row([' Daniel',    '45-39', '6', ' 535 '])


print('\n',jornadas)
print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)