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
        Jornadas: 24
        Juegos: 72
"""

info = """
    🔥🔥 INFORMACION IMPORTANTE 🔥🔥

    Vivo Jose ayer jugo un equipo
    que no jugaba en la jornada,
    por lo cual debe un juego
    y tendra que pasar por la
    voluntad POPULAR!!!
"""

title = PrettyTable(['🔥🔥 Mundial de pronosticos 🔥🔥'])
tabla_dia = PrettyTable(['Players', 'G-P', 'DIF', 'PCT %'])

tabla_dia.add_row([' #######',   '44-27', '-', ' 610 ']) 
tabla_dia.add_row([' Eduardo',   '43-29', '1', ' 600 '])
tabla_dia.add_row([' Erycherd',  '43-29', '1', ' 600 '])
tabla_dia.add_row([' Christian', '42-30', '2', ' 585 '])
tabla_dia.add_row([' Steven',    '41-31', '3', ' 570 '])
tabla_dia.add_row([' Kleydi',    '41-31', '3', ' 570 '])
tabla_dia.add_row([' Daniel',    '40-32', '4', ' 555 '])


print('\n',jornadas)
print(info)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)