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
        Jornadas: 21
        Juegos: 63           
"""

info = """
        Kleydi   debe 1
        Erycherd debe 1
"""

title = PrettyTable(['🔥🔥 Mundial de pronosticos 🔥🔥'])
tabla_dia = PrettyTable(['Players', 'G-P', 'DIF', 'PCT %'])
tabla_dia.add_row([' CarlosJ',   '39-24', '-', ' 620 ']) 
tabla_dia.add_row([' Erycherd',  '38-24', '1', ' 610 '])
tabla_dia.add_row([' Christian', '38-25', '1', ' 605 '])
tabla_dia.add_row([' Daniel',    '37-26', '2', ' 585 '])
tabla_dia.add_row([' Eduardo',   '35-28', '4', ' 555 '])
tabla_dia.add_row([' Steven',    '35-28', '4', ' 555 '])
tabla_dia.add_row([' Kleydi',    '34-28', '5', ' 540 '])



print('\n',jornadas)
print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)