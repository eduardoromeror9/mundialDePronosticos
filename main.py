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
        Jornadas: 19
        Juegos: 57

        
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

tabla_dia.add_row([' Daniel',    '36-20', '-', ' 640 '])
tabla_dia.add_row([' Christian', '36-21', '-', ' 630 '])
tabla_dia.add_row([' Erycherd',  '36-21', '-', ' 630 '])
tabla_dia.add_row([' CarlosJ',   '36-21', '-', ' 630 '])
tabla_dia.add_row([' Eduardo',   '34-23', '2', ' 595 '])
tabla_dia.add_row([' Kleydi',    '33-24', '3', ' 580 '])
tabla_dia.add_row([' Steven',    '33-24', '3', ' 580 '])



print('\n',jornadas)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(info)
print(title)
print(tabla_dia,'\n')
print(legend)