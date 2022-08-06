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
          Juegos  : 220
          Jornadas: 68
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

tabla_dia.add_row([' Eduardo',  '131-89', '-', ' 595 '])
tabla_dia.add_row([' Steven',   '131-89', '-', ' 595 '])
tabla_dia.add_row([' Kleydi',   '129-91', '2', ' 585 '])
tabla_dia.add_row([' CarlosJ',  '129-91', '2', ' 585 '])
tabla_dia.add_row([' Daniel',   '123-97', '8', ' 560 '])
tabla_dia.add_row([' Erycherd', '118-102','13',' 535 '])
tabla_dia.add_row([' Christian','117-103','14',' 530 '])


print('\n',jornadas)
# print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)
