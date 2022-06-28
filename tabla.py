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
          Jornadas: 49
          Juegos: 154
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
tabla_dia.add_row([' Eduardo',   '93-61', '-', ' 605 '])
tabla_dia.add_row([' Kleydi',    '93-61', '-', ' 605 '])
tabla_dia.add_row([' Steven',    '93-61', '-', ' 605 '])
tabla_dia.add_row([' -------',   '-----', '-', ' --- '])
tabla_dia.add_row([' CarlosJ',   '88-66', '5', ' 570 '])
tabla_dia.add_row([' Erycherd',  '87-67', '6', ' 565 '])
tabla_dia.add_row([' Daniel',    '85-69', '8', ' 550 '])
tabla_dia.add_row([' Christian', '84-70', '9', ' 545 '])


print('\n',jornadas)
print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)
