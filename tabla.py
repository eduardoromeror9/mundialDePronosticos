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
          Jornadas: 36
          Juegos: 115
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

tabla_dia.add_row([' Eduardo',   '69-46', '-', ' 600 '])
tabla_dia.add_row([' Kleydi',    '68-47', '1', ' 590 '])
tabla_dia.add_row([' Steven',    '68-47', '1', ' 590 '])
tabla_dia.add_row([' Erycherd',  '66-49', '3', ' 575 '])
tabla_dia.add_row([' CarlosJ',   '66-49', '3', ' 575 '])
tabla_dia.add_row([' Christian', '63-52', '6', ' 550 '])
tabla_dia.add_row([' Daniel',    '62-53', '7', ' 540 '])


print('\n',jornadas)
print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)
