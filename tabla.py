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
          Jornadas: 53
          Juegos: 166
"""

info = """
"""

title = PrettyTable(['🔥🔥 Mundial de pronosticos  🔥🔥'])

tabla_dia = PrettyTable(['Players', 'G-P', 'DIF', 'PCT %'])

tabla_dia.add_row([' Kleydi',    '100-66', '-', ' 600 '])
tabla_dia.add_row([' Eduardo',   '99-67', '1', ' 595 '])
tabla_dia.add_row([' Steven',    '99-67', '1', ' 595 '])
tabla_dia.add_row([' CarlosJ',   '98-68', '2', ' 590 '])
tabla_dia.add_row([' Daniel',    '95-71', '5', ' 570 '])
tabla_dia.add_row([' Erycherd',  '93-73', '7', ' 560 '])
tabla_dia.add_row([' Christian', '93-73', '7', ' 560 '])


print('\n',jornadas)
# print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)
