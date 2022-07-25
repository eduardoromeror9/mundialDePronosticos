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
          Jornadas: 62
          Juegos: 199
          CR96 debe 3
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

tabla_dia.add_row([' Steven',    '119-80', '-', ' 600 '])
tabla_dia.add_row([' CarlosJ',   '119-80', '-', ' 600 '])
tabla_dia.add_row([' Eduardo',   '118-81', '1', ' 590 '])
tabla_dia.add_row([' Kleydi',    '116-83', '3', ' 580 '])
tabla_dia.add_row([' Daniel*',   '111-88', '8', ' 555 '])
tabla_dia.add_row([' Erycherd',  '109-90', '10', '545 '])
tabla_dia.add_row([' Christian', '105-91', '14',' 535 '])


print('\n',jornadas)
print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)
