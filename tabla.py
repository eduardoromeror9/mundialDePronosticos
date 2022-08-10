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
          Juegos  : 226
          Jornadas: 70
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

tabla_dia.add_row([' Eduardo',  '135-91', '-', ' 595 '])
tabla_dia.add_row([' Steven',   '134-92', '1', ' 590 '])
tabla_dia.add_row([' Kleydi',   '132-94', '3', ' 585 '])
tabla_dia.add_row([' CarlosJ',  '132-94', '3', ' 585 '])
tabla_dia.add_row([' Daniel',   '126-100','9', ' 555 '])
tabla_dia.add_row([' Christian','119-107','16',' 525 '])
tabla_dia.add_row([' Erycherd', '118-105','17',' 530 '])


print('\n',jornadas)
# print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)
