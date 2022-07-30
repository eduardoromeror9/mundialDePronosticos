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
          Juegos  : 208
          Jornadas: 65
          Erycherd debe 3
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

tabla_dia.add_row([' Steven',    '123-85', '-', ' 585 '])
tabla_dia.add_row([' Eduardo',   '122-86', '1', ' 580 '])
tabla_dia.add_row([' CarlosJ',   '122-86', '1', ' 580 '])
tabla_dia.add_row([' Kleydi',    '120-88', '3', ' 570 '])
tabla_dia.add_row([' Daniel',    '115-93', '8', ' 545 '])
tabla_dia.add_row([' Erycherd',  '111-94', '9', ' 540 '])
tabla_dia.add_row([' Christian', '107-101','16',' 515 '])


print('\n',jornadas)
print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)
