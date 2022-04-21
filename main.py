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
            Jornadas: 9
            Juegos: 27            
            CR96: Debe 7*
"""

title = PrettyTable(['🔥🔥 Mundial de pronosticos 🔥🔥'])
tabla_dia = PrettyTable(['Players', 'G-P', 'DIF', 'PCT %'])

tabla_dia.add_row(['Daniel',     '17-10', '-', ' 630 '])
tabla_dia.add_row(['CarlosJ',    '17-10', '-', ' 630 '])
tabla_dia.add_row(['Christian*', '16-04', '1', ' 800 '])
tabla_dia.add_row(['Erycherd',   '15-12', '2', ' 555 '])
tabla_dia.add_row(['Eduardo',    '14-13', '3', ' 520 '])
tabla_dia.add_row(['Kleydi',     '14-13', '3', ' 520 '])
tabla_dia.add_row(['Steven',     '13-14', '4', ' 480 '])


print('\n',jornadas)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)