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
          Jornadas: 39
          Juegos: 124
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

tabla_dia.add_row([' Eduardo',   '74-50', '-', ' 595 '])
tabla_dia.add_row([' Steven',    '74-50', '-', ' 595 '])
tabla_dia.add_row([' Kleydi',    '73-51', '1', ' 585 '])
tabla_dia.add_row([' CarlosJ',   '73-51', '1', ' 585 '])
tabla_dia.add_row([' Erycherd',  '72-52', '2', ' 580 '])
tabla_dia.add_row([' Christian', '69-55', '5', ' 555 '])
tabla_dia.add_row([' Daniel',    '67-57', '7', ' 540 '])


print('\n',jornadas)
print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)
