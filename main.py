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
          Jornadas: 25
          Juegos: 75
"""

info = """
"""

title = PrettyTable(['🔥🔥 Mundial de pronosticos 🔥🔥'])
tabla_dia = PrettyTable(['Players', 'G-P', 'DIF', 'PCT %'])

tabla_dia.add_row([' Eduardo',   '45-30', '-', ' 600 '])
tabla_dia.add_row([' Erycherd',  '44-31', '1', ' 585 '])
tabla_dia.add_row([' CarlosJ',   '44-31', '1', ' 585 '])
tabla_dia.add_row([' Christian', '43-32', '2', ' 575 '])
tabla_dia.add_row([' Kleydi',    '42-33', '3', ' 560 '])
tabla_dia.add_row([' Steven',    '41-34', '4', ' 545 '])
tabla_dia.add_row([' Daniel',    '41-34', '4', ' 545 '])


print('\n',jornadas)
# print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)