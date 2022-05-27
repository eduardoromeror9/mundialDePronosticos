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
          Jornadas: 30
          Juegos: 97
"""

info = """
  🧊🧊 Kleydi a la NEVERA 🧊🧊
  🧊🧊 Kleydi a la NEVERA 🧊🧊
  🧊🧊 Kleydi a la NEVERA 🧊🧊
  🧊🧊 Kleydi a la NEVERA 🧊🧊
  🧊🧊 Kleydi a la NEVERA 🧊🧊
  🧊🧊 Kleydi a la NEVERA 🧊🧊
"""

title = PrettyTable(['🔥🔥 Mundial de pronosticos 🔥🔥'])
tabla_dia = PrettyTable(['Players', 'G-P', 'DIF', 'PCT %'])

tabla_dia.add_row([' Kleydi',    '58-39', '-', ' 595 '])
tabla_dia.add_row([' Eduardo',   '57-40', '1', ' 590 '])
tabla_dia.add_row([' Erycherd',  '54-43', '4', ' 555 '])
tabla_dia.add_row([' CarlosJ',   '54-43', '4', ' 555 '])
tabla_dia.add_row([' Steven',    '53-44', '5', ' 545 '])
tabla_dia.add_row([' Christian', '53-44', '5', ' 545 '])
tabla_dia.add_row([' Daniel',    '50-47', '8', ' 515 '])


print('\n',jornadas)
print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)