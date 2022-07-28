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
          Juegos  : 205
          Jornadas: 64
"""

info = """
🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊
🧊                                🧊
🧊      CarlosJ a la NEVERA       🧊
🧊      Steven a la NEVERA        🧊  
🧊                                🧊
🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊
        
"""

title = PrettyTable(['🔥🔥 Mundial de pronosticos  🔥🔥'])
tabla_dia = PrettyTable(['Players', 'G-P', 'DIF', 'PCT %'])

tabla_dia.add_row([' Steven',    '120-85', '-', ' 585 '])
tabla_dia.add_row([' Eduardo',   '119-86', '1', ' 580 '])
tabla_dia.add_row([' CarlosJ',   '119-86', '1', ' 580 '])
tabla_dia.add_row([' Kleydi',    '117-88', '3', ' 570 '])
tabla_dia.add_row([' Daniel*',   '112-93', '8', ' 545 '])
tabla_dia.add_row([' Erycherd',  '111-94', '9', ' 540 '])
tabla_dia.add_row([' Christian', '106-99', '14',' 515 '])


print('\n',jornadas)
print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)
