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
          Jornadas: 60
          Juegos: 193

          Juegos Pendientes:
          Steven: 2
          Eduardo: 2
          Daniel: 2
          El resto: 1
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

tabla_dia.add_row([' Steven',    '114-77', '-', ' 605 '])
tabla_dia.add_row([' CarlosJ',   '114-78', '/', ' 600 '])
tabla_dia.add_row([' Eduardo',   '113-77', '1', ' 595 '])
tabla_dia.add_row([' Kleydi',    '111-81', '3', ' 595 '])
tabla_dia.add_row([' Daniel*',   '107-84', '7', ' 565 '])
tabla_dia.add_row([' Erycherd',  '106-86', '8', ' 550 '])
tabla_dia.add_row([' Christian', '103-89', '11',' 530 '])


print('\n',jornadas)
print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)
