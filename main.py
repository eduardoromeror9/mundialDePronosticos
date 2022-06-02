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
          
          Steven, Kleydi 
          y Mi bella Genio

          deben 1 juego
"""

info = """
  🧊🧊 Kleydi a la NEVERA 🧊🧊
  🧊🧊 Steven a la NEVERA 🧊🧊
"""

title = PrettyTable(['🔥🔥 Mundial de pronosticos 🔥🔥'])
tabla_dia = PrettyTable(['Players', 'G-P', 'DIF', 'PCT %'])

tabla_dia.add_row([' Eduardo',   '66-43', '-', ' 605 '])
tabla_dia.add_row([' Kleydi',    '65-43', '1', ' 595 '])
tabla_dia.add_row([' Steven',    '62-46', '4', ' 570 '])
tabla_dia.add_row([' CarlosJ',   '60-48', '6', ' 550 '])
tabla_dia.add_row([' Erycherd',  '60-49', '6', ' 550 '])
tabla_dia.add_row([' Daniel',    '59-50', '7', ' 540 '])
tabla_dia.add_row([' Christian', '59-50', '7', ' 540 '])


print('\n',jornadas)
print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)
