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
          Jornadas: 42
          Juegos: 133
"""

info = """
🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊
🧊                                🧊
🧊      Kleydi a la NEVERA        🧊
🧊      CarlosJ a la NEVERA       🧊  
🧊      Steven a la NEVERA        🧊
🧊                                🧊
🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊


"""

title = PrettyTable(['🔥🔥 Mundial de pronosticos 🔥🔥'])
tabla_dia = PrettyTable(['Players', 'G-P', 'DIF', 'PCT %'])

tabla_dia.add_row([' Steven',    '81-52', '-', ' 610 '])
tabla_dia.add_row([' Eduardo',   '80-53', '1', ' 605 '])
tabla_dia.add_row([' Kleydi',    '80-53', '1', ' 605 '])
tabla_dia.add_row([' Erycherd',  '78-55', '3', ' 585 '])
tabla_dia.add_row([' CarlosJ',   '77-56', '4', ' 580 '])
tabla_dia.add_row([' Daniel',    '73-60', '8', ' 545 '])
tabla_dia.add_row([' Christian', '73-60', '8', ' 545 '])


print('\n',jornadas)
print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)
