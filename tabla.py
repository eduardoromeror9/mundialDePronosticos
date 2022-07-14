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
          Jornadas: 58
          Juegos: 181
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

tabla_dia.add_row([' Steven',    '110-71', '-', ' 605 '])
tabla_dia.add_row([' CarlosJ',   '108-73', '2', ' 595 '])
tabla_dia.add_row([' Eduardo',   '107-74', '3', ' 590 '])
tabla_dia.add_row([' Kleydi',    '107-74', '3', ' 590 '])
tabla_dia.add_row([' Daniel*',   '103-78', '7', ' 570 '])
tabla_dia.add_row([' Erycherd',  '100-81', '10',' 550 '])
tabla_dia.add_row([' Christian', '96-85',  '14',' 530 '])


print('\n',jornadas)
print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)
