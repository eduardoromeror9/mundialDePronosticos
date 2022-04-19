from prettytable import PrettyTable

legend = """
 🔥🔥 INFORMACION IMPORTANTE 🔥🔥
 Don Eduardo Romero,
 mejor conocido como 
 el KING de los PRONOSTICOS
 ES EL VIGENTE CAMPEON
 HASTA QUE SE DEMUESTRE LO CONTRARIO
  \n"""

jornadas = """  
            Jornadas: 8
            Juegos: 24
            CR96: Debe 21
"""

title = PrettyTable(['🔥🔥 Mundial de pronosticos 🔥🔥'])
tabla_dia = PrettyTable(['Players', 'G-P', 'DIF', 'PCT %'])

tabla_dia.add_row(['Daniel',    '15-09', '-', ' 625  '])
tabla_dia.add_row(['Erycherd',  '15-09', '-', ' 625  '])
tabla_dia.add_row(['CarlosJ',   '15-09', '-', ' 625  '])
tabla_dia.add_row(['Kleydi',    '14-10', '1', ' 583  '])
tabla_dia.add_row(['Eduardo',   '11-13', '4', ' 460  '])
tabla_dia.add_row(['Steven',    '11-13', '4', ' 460  '])
tabla_dia.add_row(['Christian', '03-01', '∞', ' ---  '])


print('\n',jornadas)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)