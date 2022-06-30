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
          Jornadas: 50
          Juegos: 157
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
tabla_dia.add_row([' Kleydi',    '95-62', '-', ' 605 '])
tabla_dia.add_row([' Eduardo',   '94-63', '1', ' 600 '])
tabla_dia.add_row([' Steven',    '94-63', '1', ' 600 '])
tabla_dia.add_row([' -------',   '-----', '-', ' --- '])
tabla_dia.add_row([' CarlosJ',   '90-67', '5', ' 575 '])
tabla_dia.add_row([' Erycherd',  '89-68', '6', ' 565 '])
tabla_dia.add_row([' Daniel',    '87-70', '8', ' 555 '])
tabla_dia.add_row([' Christian', '87-70', '8', ' 555 '])
# tabla_dia.add_row([' Christian', '86-71', '9', ' 545 '])


print('\n',jornadas)
print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)
