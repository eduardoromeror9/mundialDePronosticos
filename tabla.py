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
          Jornadas: 61
          Juegos: 196
"""

info = """
🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊
🧊                                🧊
🧊      CarlosJ a la NEVERA       🧊
🧊      Steven a la NEVERA        🧊  
🧊                                🧊
🧊                                🧊
🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊
        
"""

title = PrettyTable(['🔥🔥 Mundial de pronosticos  🔥🔥'])

tabla_dia = PrettyTable(['Players', 'G-P', 'DIF', 'PCT %'])

tabla_dia.add_row([' Steven',    '116-80', '-', ' 590 '])
tabla_dia.add_row([' CarlosJ',   '116-80', '-', ' 590 '])
tabla_dia.add_row([' Eduardo',   '115-81', '1', ' 585 '])
tabla_dia.add_row([' Kleydi',    '113-83', '3', ' 575 '])
tabla_dia.add_row([' Daniel*',   '110-86', '6', ' 560 '])
tabla_dia.add_row([' Erycherd',  '108-88', '8', ' 550 '])
tabla_dia.add_row([' Christian', '105-91', '11',' 535 '])


print('\n',jornadas)
print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)
