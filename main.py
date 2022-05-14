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
        Jornadas: 22
        Juegos: 66
"""

info = """
        🚩🚩🚩
        Erycherd quiere
        ir a consulta
        por 4 juegos
        que debe
        tuvo 38733
        oportunidades
        de jugarlos 🚩🚩🚩
"""

title = PrettyTable(['🔥🔥 Mundial de pronosticos 🔥🔥'])
tabla_dia = PrettyTable(['Players', 'G-P', 'DIF', 'PCT %'])
tabla_dia.add_row([' #######',   '41-25', '-', ' 620 ']) 
tabla_dia.add_row([' Erycherd',  '40-26', '1', ' 605 '])
tabla_dia.add_row([' Christian', '39-27', '3', ' 590 '])
tabla_dia.add_row([' Daniel',    '39-27', '2', ' 590 '])
tabla_dia.add_row([' Eduardo',   '38-28', '3', ' 575 '])
tabla_dia.add_row([' Steven',    '38-28', '3', ' 575 '])
tabla_dia.add_row([' Kleydi',    '38-28', '3', ' 575 '])



print('\n',jornadas)
print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)