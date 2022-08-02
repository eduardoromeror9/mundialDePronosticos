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
          Juegos  : 214
          Jornadas: 66
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

title = PrettyTable(['🔥🔥 Mundial de pronosticos  🔥🔥 '])
tabla_dia = PrettyTable(['Players', 'G-P', 'DIF', 'PCT %'])

tabla_dia.add_row([' Eduardo',   '127-87', '-', ' 595 '])
tabla_dia.add_row([' CarlosJ',   '127-87', '-', ' 595 '])
tabla_dia.add_row([' Steven',    '126-88', '1', ' 590 '])
tabla_dia.add_row([' Kleydi',    '124-90', '3', ' 580 '])
tabla_dia.add_row([' Daniel',    '119-95', '8', ' 555 '])
tabla_dia.add_row([' Erycherd',  '114-97', '13',' 540 '])
tabla_dia.add_row([' Christian', '112-102','15',' 520 '])


print('\n',jornadas)
print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)
