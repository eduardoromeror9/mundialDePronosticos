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
          Jornadas: 38
          Juegos: 121
"""

info = """
🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊
🧊                                🧊
🧊                                🧊
🧊      Kleydi a la NEVERA        🧊
🧊      Kleydi a la NEVERA        🧊
🧊                                🧊
🧊      Steven a la NEVERA        🧊  
🧊      Steven a la NEVERA        🧊
🧊                                🧊
🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊


"""

title = PrettyTable(['🔥🔥 Mundial de pronosticos 🔥🔥'])
tabla_dia = PrettyTable(['Players', 'G-P', 'DIF', 'PCT %'])

tabla_dia.add_row([' Eduardo',   '72-49', '-', ' 595 '])
tabla_dia.add_row([' Kleydi',    '71-50', '1', ' 585 '])
tabla_dia.add_row([' Steven',    '71-50', '1', ' 585 '])
tabla_dia.add_row([' Erycherd',  '70-51', '2', ' 580 '])
tabla_dia.add_row([' CarlosJ',   '70-51', '2', ' 580 '])
tabla_dia.add_row([' Christian', '66-55', '6', ' 545 '])
tabla_dia.add_row([' Daniel',    '65-56', '7', ' 540 '])


print('\n',jornadas)
print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)
