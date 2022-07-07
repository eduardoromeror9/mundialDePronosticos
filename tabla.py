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
          Jornadas: 54
          Juegos: 169
"""

info = """
"""

title = PrettyTable(['🔥🔥 Mundial de pronosticos  🔥🔥'])

tabla_dia = PrettyTable(['Players', 'G-P', 'DIF', 'PCT %'])

tabla_dia.add_row([' Kleydi',    '103-66', '-', ' 610 '])
tabla_dia.add_row([' Steven',    '101-68', '2', ' 595 '])
tabla_dia.add_row([' CarlosJ',   '101-68', '2', ' 595 '])
tabla_dia.add_row([' Eduardo',   '100-69', '3', ' 590 '])
tabla_dia.add_row([' Daniel',    '97-72',  '6', ' 575 '])
tabla_dia.add_row([' Erycherd',  '95-74',  '8', ' 560 '])
tabla_dia.add_row([' Christian', '95-74',  '8', ' 560 '])


print('\n',jornadas)
# print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)
