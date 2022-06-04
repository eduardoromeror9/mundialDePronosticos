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
          Jornadas: 35
          Juegos: 112
"""

info = """
  🧊🧊 Kleydi a la NEVERA 🧊🧊
  🧊🧊 Steven a la NEVERA 🧊🧊
"""

title = PrettyTable(['🔥🔥 Mundial de pronosticos 🔥🔥'])
tabla_dia = PrettyTable(['Players', 'G-P', 'DIF', 'PCT %'])

tabla_dia.add_row([' Eduardo',   '68-44', '-', ' 605 '])
tabla_dia.add_row([' Kleydi',    '66-46', '2', ' 590 '])
tabla_dia.add_row([' Steven',    '66-46', '2', ' 590 '])
tabla_dia.add_row([' Erycherd',  '63-49', '5', ' 560 '])
tabla_dia.add_row([' CarlosJ',   '63-49', '5', ' 560 '])
tabla_dia.add_row([' Daniel',    '62-50', '6', ' 555 '])
tabla_dia.add_row([' Christian', '62-50', '6', ' 555 '])


print('\n',jornadas)
print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)
