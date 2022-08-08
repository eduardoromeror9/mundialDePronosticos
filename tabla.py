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
          Juegos  : 223
          Jornadas: 69
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

tabla_dia.add_row([' Eduardo',  '133-90', '-', ' 595 '])
tabla_dia.add_row([' Steven',   '131-92', '2', ' 585 '])
tabla_dia.add_row([' CarlosJ',  '130-93', '3', ' 580 '])
tabla_dia.add_row([' Kleydi',   '129-94', '4', ' 575 '])
tabla_dia.add_row([' Daniel',   '123-100','10',' 550 '])
tabla_dia.add_row([' Erycherd', '118-105','15',' 530 '])
tabla_dia.add_row([' Christian','117-106','16',' 525 '])


print('\n',jornadas)
# print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)
