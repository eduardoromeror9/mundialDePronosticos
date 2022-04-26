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
        Jornadas: 12
        Juegos: 36

        
        Carlos Jose cree
        que va a ganar
        pero ese no le gana
        ni a paquito
        jugando reloj

        Steven dando LASTIMA
            
"""

title = PrettyTable(['🔥🔥 Mundial de pronosticos 🔥🔥'])
tabla_dia = PrettyTable(['Players', 'G-P', 'DIF', 'PCT %'])

tabla_dia.add_row([' Christian',   '24-12', '-', ' 665 '])
tabla_dia.add_row([' Daniel',      '23-13', '1', ' 640 '])
tabla_dia.add_row([' CarlosJ',     '22-14', '2', ' 610 '])
tabla_dia.add_row([' Eduardo',     '21-15', '3', ' 585 '])
tabla_dia.add_row([' Erycherd',    '21-15', '3', ' 585 '])
tabla_dia.add_row([' Kleydi',      '19-17', '5', ' 530 '])
tabla_dia.add_row([' Steven',      '16-20', '8', ' 445 '])



print('\n',jornadas)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)