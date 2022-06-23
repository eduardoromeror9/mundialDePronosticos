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
          Jornadas: 46
          Juegos: 145
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

tabla_dia.add_row([' Eduardo',   '88-57', '-', ' 605 '])
tabla_dia.add_row([' Kleydi',    '88-57', '-', ' 605 '])
tabla_dia.add_row([' Steven',    '88-57', '-', ' 605 '])
tabla_dia.add_row([' -------',   '-----', '#', ' --- '])
tabla_dia.add_row([' laOtraLiga',   '#####', '#', ' ### '])
tabla_dia.add_row([' -------',   '-----', '#', ' --- '])
tabla_dia.add_row([' CarlosJ',   '83-62', '5', ' 570 '])
tabla_dia.add_row([' Erycherd',  '82-63', '6', ' 565 '])
tabla_dia.add_row([' Daniel',    '81-64', '7', ' 560 '])
tabla_dia.add_row([' Christian', '81-64', '7', ' 560 '])


print('\n',jornadas)
print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)
