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
          Jornadas: 31
          Juegos: 100

      EL niño especial debe 1
"""

info = """
  🧊🧊 Kleydi a la NEVERA 🧊🧊
  🧊🧊 Kleydi a la NEVERA 🧊🧊
"""

title = PrettyTable(['🔥🔥 Mundial de pronosticos 🔥🔥'])
tabla_dia = PrettyTable(['Players', 'G-P', 'DIF', 'PCT %'])

tabla_dia.add_row([' Kleydi',    '60-40', '-', ' 600 '])
tabla_dia.add_row([' Eduardo',   '58-42', '2', ' 580 '])
tabla_dia.add_row([' CarlosJ',   '57-43', '3', ' 570 '])
tabla_dia.add_row([' Erycherd',  '55-44', '5', ' 550 '])
tabla_dia.add_row([' Steven',    '55-45', '5', ' 550 '])
tabla_dia.add_row([' Christian', '54-46', '6', ' 540 '])
tabla_dia.add_row([' Daniel',    '51-49', '9', ' 510 '])


print('\n',jornadas)
print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)