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
        Jornadas: 13
        Juegos: 39

        
        Carlos Jose cree
        que va a ganar
        pero ese no le gana
        ni a paquito
        jugando reloj
            
"""

title = PrettyTable(['🔥🔥 Mundial de pronosticos 🔥🔥'])
tabla_dia = PrettyTable(['Players', 'G-P', 'DIF', 'PCT %'])

tabla_dia.add_row([' Daniel',      '25-14', '-', ' 640 '])
tabla_dia.add_row([' Christian',   '25-14', '-', ' 640 '])
tabla_dia.add_row([' CarlosJ',     '24-15', '1', ' 615 '])
tabla_dia.add_row([' Erycherd',    '23-16', '2', ' 590 '])
tabla_dia.add_row([' Eduardo',     '22-17', '3', ' 565 '])
tabla_dia.add_row([' Kleydi',      '21-18', '4', ' 540 '])
tabla_dia.add_row([' Steven',      '19-20', '6', ' 490 '])



print('\n',jornadas)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)