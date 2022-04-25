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
        Jornadas: 11
        Juegos: 33

        
        Carlos Jose cree
        que va a ganar
        pero ese no le gana
        ni a paquito
        jugando reloj
            
"""

title = PrettyTable(['🔥🔥 Mundial de pronosticos 🔥🔥'])
tabla_dia = PrettyTable(['Players', 'G-P', 'DIF', 'PCT %'])

tabla_dia.add_row([' Daniel',      '21-12', '-', ' 635 '])
tabla_dia.add_row([' Christian',   '21-12', '-', ' 635 '])
tabla_dia.add_row([' CarlosJ',     '21-12', '-', ' 635 '])
tabla_dia.add_row([' Eduardo',     '19-14', '2', ' 575 '])
tabla_dia.add_row([' Erycherd',    '19-14', '2', ' 575 '])
tabla_dia.add_row([' Kleydi',      '17-16', '4', ' 515 '])
tabla_dia.add_row([' Steven',      '15-18', '6', ' 455 '])



print('\n',jornadas)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)