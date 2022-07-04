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
          Jornadas: 52
          Juegos: 163
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
tabla_dia.add_row([' Eduardo',   '98-65', '-', ' 600 '])
tabla_dia.add_row([' Kleydi',    '98-65', '-', ' 600 '])
tabla_dia.add_row([' Steven',    '97-66', '1', ' 595 '])
tabla_dia.add_row([' ------',       '-----', '-', ' --- '])
tabla_dia.add_row([' losMalos',   '↓↓↓↓↓', '↓', ' ↓↓↓ '])
tabla_dia.add_row([' ------',       '-----', '-', ' --- '])
tabla_dia.add_row([' CarlosJ',   '95-68', '3', ' 580 '])
tabla_dia.add_row([' Daniel',    '92-71', '6', ' 565 '])
tabla_dia.add_row([' Erycherd',  '91-72', '7', ' 560 '])
tabla_dia.add_row([' Christian', '91-72', '7', ' 560 '])


print('\n',jornadas)
print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)
