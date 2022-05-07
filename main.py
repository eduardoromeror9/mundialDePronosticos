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
        Jornadas: 18
        Juegos: 54

        
        Carlos Jose cree
        que va a ganar
        pero ese no le gana
        ni a paquito
        jugando reloj
            
"""

info = """
     Le informo a los ilusos que
     no gana el 
     que LE GANE AL KING
     Gana el que va PRIMERO!!

     Daniel debe 1!!
"""

title = PrettyTable(['🔥🔥 Mundial de pronosticos 🔥🔥'])
tabla_dia = PrettyTable(['Players', 'G-P', 'DIF', 'PCT %'])

tabla_dia.add_row([' Christian', '35-19', '-', ' 650 '])
tabla_dia.add_row([' Erycherd',  '35-19', '-', ' 650 '])
tabla_dia.add_row([' Daniel',    '34-19', '1', ' 630 '])
tabla_dia.add_row([' CarlosJ',   '33-21', '3', ' 610 '])
tabla_dia.add_row([' Eduardo',   '32-22', '3', ' 590 '])
tabla_dia.add_row([' Kleydi',    '32-22', '3', ' 590 '])
tabla_dia.add_row([' Steven',    '30-24', '5', ' 555 '])



print('\n',jornadas)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(info)
print(title)
print(tabla_dia,'\n')
print(legend)