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
          Jornadas: 45
          Juegos: 142
"""

info = """
🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊
🧊                                🧊
🧊      Kleydi a la NEVERA        🧊
🧊      Steven a la NEVERA        🧊
🧊                                🧊
🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊


"""

title = PrettyTable(['🔥🔥 Mundial de pronosticos  🔥🔥'])
tabla_dia = PrettyTable(['Players', 'G-P', 'DIF', 'PCT %'])

tabla_dia.add_row([' Steven',    '86-56', '-', ' 605 '])
tabla_dia.add_row([' Eduardo',   '85-57', '1', ' 600 '])
tabla_dia.add_row([' Kleydi',    '85-57', '1', ' 600 '])
tabla_dia.add_row([' CarlosJ',   '81-61', '5', ' 570 '])
tabla_dia.add_row([' Erycherd',  '80-62', '6', ' 560 '])
tabla_dia.add_row([' Christian', '79-63', '7', ' 555 '])
tabla_dia.add_row([' Daniel',    '78-64', '8', ' 550 '])


print('\n',jornadas)
print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)
