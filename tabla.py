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
          Juegos  : 229
          Jornadas: 71
          Christian debe 1
          Erycherd debe 1
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

tabla_dia.add_row([' Eduardo',  '137-92', '-', ' 600 '])
tabla_dia.add_row([' Steven',   '135-94', '2', ' 590 '])
tabla_dia.add_row([' Kleydi',   '133-96', '4', ' 580 '])
tabla_dia.add_row([' CarlosJ',  '133-96', '4', ' 580 '])
tabla_dia.add_row([' Daniel',   '127-102','10',' 555 '])
tabla_dia.add_row([' Erycherd', '121-107','16',' 530 '])
tabla_dia.add_row([' Christian','120-108','17',' 525 '])


print('\n',jornadas)
# print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)
