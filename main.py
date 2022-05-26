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
          Jornadas: 29
          Juegos: 87
"""

info = """
  🧊🧊 Kleydi a la NEVERA 🧊🧊
"""

title = PrettyTable(['🔥🔥 Mundial de pronosticos 🔥🔥'])
tabla_dia = PrettyTable(['Players', 'G-P', 'DIF', 'PCT %'])

tabla_dia.add_row([' Eduardo',   '52-35', '-', ' 600 '])
tabla_dia.add_row([' Kleydi',    '52-35', '-', ' 600 '])
tabla_dia.add_row([' Erycherd',  '50-37', '2', ' 575 '])
tabla_dia.add_row([' Christian', '49-38', '3', ' 565 '])
tabla_dia.add_row([' CarlosJ',   '49-38', '3', ' 565 '])
tabla_dia.add_row([' Steven',    '47-40', '5', ' 540 '])
tabla_dia.add_row([' Daniel',    '47-40', '5', ' 540 '])


print('\n',jornadas)
print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)