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
          Juegos  : 217
          Jornadas: 67
          Daniel debe 1
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

tabla_dia.add_row([' Eduardo',  '129-88', '-', ' 595 '])
tabla_dia.add_row([' Steven',   '128-89', '1', ' 590 '])
tabla_dia.add_row([' CarlosJ',  '128-89', '1', ' 590 '])
tabla_dia.add_row([' Kleydi',   '127-90', '2', ' 580 '])
tabla_dia.add_row([' Daniel',   '120-95', '9', ' 555 '])
tabla_dia.add_row([' Erycherd', '117-100','12',' 540 '])
tabla_dia.add_row([' Christian','115-102','14',' 530 '])


print('\n',jornadas)
print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)
