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
          Jornadas: 51
          Juegos: 160
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
tabla_dia.add_row([' Eduardo',   '97-63', '-', ' 605 '])
tabla_dia.add_row([' Kleydi',    '96-64', '1', ' 600 '])
tabla_dia.add_row([' Steven',    '96-64', '1', ' 600 '])
tabla_dia.add_row([' -------',   '-----', '-', ' --- '])
tabla_dia.add_row([' CarlosJ',   '93-67', '4', ' 580 '])
tabla_dia.add_row([' Daniel',    '90-70', '7', ' 560 '])
tabla_dia.add_row([' Erycherd',  '90-70', '7', ' 560 '])
tabla_dia.add_row([' Christian', '89-71', '8', ' 555 '])


print('\n',jornadas)
print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)
