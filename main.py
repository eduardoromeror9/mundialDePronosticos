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
          Jornadas: 34
          Juegos: 109
"""

info = """
  🧊🧊 Kleydi a la NEVERA 🧊🧊
  🧊🧊 Kleydi a la NEVERA 🧊🧊
"""

title = PrettyTable(['🔥🔥 Mundial de pronosticos 🔥🔥'])
tabla_dia = PrettyTable(['Players', 'G-P', 'DIF', 'PCT %'])

tabla_dia.add_row([' Kleydi',    '64-42', '-', ' 600 '])
tabla_dia.add_row([' Eduardo',   '63-43', '1', ' 595 '])
tabla_dia.add_row([' Steven',    '60-46', '4', ' 565 '])
tabla_dia.add_row([' CarlosJ',   '59-47', '5', ' 555 '])
tabla_dia.add_row([' Erycherd',  '58-48', '6', ' 545 '])
tabla_dia.add_row([' Christian', '57-49', '6', ' 535 '])
tabla_dia.add_row([' Daniel',    '56-50', '8', ' 530 '])


print('\n',jornadas)
print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)
