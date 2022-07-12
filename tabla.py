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
          Jornadas: 57
          Juegos: 178
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

tabla_dia.add_row([' Steven',    '107-71', '-', ' 600 '])
tabla_dia.add_row([' Kleydi',    '106-72', '1', ' 595 '])
tabla_dia.add_row([' CarlosJ',   '105-73', '2', ' 590 '])
tabla_dia.add_row([' Eduardo',   '104-74', '3', ' 585 '])
tabla_dia.add_row([' Daniel',    '100-78', '7', ' 560 '])
tabla_dia.add_row([' Erycherd',  '99-79',  '8', ' 555 '])
tabla_dia.add_row([' Christian', '96-82',  '11',' 540 '])


print('\n',jornadas)
print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)
