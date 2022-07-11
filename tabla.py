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
          Jornadas: 56
          Juegos: 175
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

title = PrettyTable(['🔥🔥 Mundial de pronosticos  🔥🔥'])

tabla_dia = PrettyTable(['Players', 'G-P', 'DIF', 'PCT %'])

tabla_dia.add_row([' Steven',    '105-70', '-', ' 600 '])
tabla_dia.add_row([' Kleydi',    '105-70', '-', ' 600 '])
tabla_dia.add_row([' CarlosJ',   '104-71', '1', ' 595 '])
tabla_dia.add_row([' Eduardo',   '102-73', '3', ' 580 '])
tabla_dia.add_row([' Daniel',    '99-76',  '6', ' 565 '])
tabla_dia.add_row([' Erycherd',  '98-77',  '7', ' 560 '])
tabla_dia.add_row([' Christian', '95-80',  '10',' 540 '])


print('\n',jornadas)
print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)
