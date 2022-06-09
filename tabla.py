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
          Jornadas: 37
          Juegos: 118
"""

info = """
🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊
🧊                                🧊
🧊                                🧊
🧊      Kleydi a la NEVERA        🧊
🧊      Kleydi a la NEVERA        🧊
🧊      Kleydi a la NEVERA        🧊
🧊      Kleydi a la NEVERA        🧊
🧊                                🧊
🧊                                🧊  
🧊                                🧊
🧊                                🧊
🧊                                🧊
🧊                                🧊 
🧊      Steven a la NEVERA        🧊
🧊      Steven a la NEVERA        🧊
🧊      Steven a la NEVERA        🧊
🧊      Steven a la NEVERA        🧊  
🧊                                🧊
🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊


"""

title = PrettyTable(['🔥🔥 Mundial de pronosticos 🔥🔥'])
tabla_dia = PrettyTable(['Players', 'G-P', 'DIF', 'PCT %'])

tabla_dia.add_row([' Eduardo',   '70-48', '-', ' 600 '])
tabla_dia.add_row([' Kleydi',    '70-48', '-', ' 590 '])
tabla_dia.add_row([' Steven',    '69-49', '1', ' 590 '])
tabla_dia.add_row([' CarlosJ',   '68-50', '2', ' 575 '])
tabla_dia.add_row([' Erycherd',  '67-50', '3', ' 575 '])
tabla_dia.add_row([' Christian', '64-54', '6', ' 550 '])
tabla_dia.add_row([' Daniel',    '63-55', '7', ' 540 '])


print('\n',jornadas)
print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)
