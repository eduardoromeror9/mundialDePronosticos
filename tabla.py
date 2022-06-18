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
          Jornadas: 43
          Juegos: 136
"""

info = """
🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊
🧊                                🧊
🧊      Kleydi a la NEVERA        🧊
🧊      Steven a la NEVERA        🧊
🧊                                🧊
🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊


"""

title = PrettyTable(['🔥🔥 Mundial de pronosticos 🔥🔥'])
tabla_dia = PrettyTable(['Players', 'G-P', 'DIF', 'PCT %'])

tabla_dia.add_row([' Kleydi',    '83-53', '-', ' 610 '])
tabla_dia.add_row([' Steven',    '83-53', '-', ' 610 '])
tabla_dia.add_row([' Eduardo',   '82-54', '1', ' 605 '])
tabla_dia.add_row([' Erycherd',  '79-57', '4', ' 580 '])
tabla_dia.add_row([' CarlosJ',   '78-58', '5', ' 580 '])
tabla_dia.add_row([' Daniel',    '75-61', '8', ' 550 '])
tabla_dia.add_row([' Christian', '74-62', '9', ' 545 '])


print('\n',jornadas)
print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)
