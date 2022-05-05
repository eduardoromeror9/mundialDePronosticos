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
        Jornadas: 17
        Juegos: 51

        
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

     Vivin debe 1, va a consulta!!
"""

title = PrettyTable(['🔥🔥 Mundial de pronosticos 🔥🔥'])
tabla_dia = PrettyTable(['Players', 'G-P', 'DIF', 'PCT %'])

tabla_dia.add_row([' Christian', '33-17', '-', ' 645 '])
tabla_dia.add_row([' Erycherd',  '32-19', '1', ' 630 '])
tabla_dia.add_row([' Daniel',    '32-19', '1', ' 630 '])
tabla_dia.add_row([' Eduardo',   '30-21', '3', ' 590 '])
tabla_dia.add_row([' CarlosJ',   '30-21', '3', ' 590 '])
tabla_dia.add_row([' Kleydi',    '29-22', '4', ' 570 '])
tabla_dia.add_row([' Steven',    '27-24', '6', ' 530 '])



print('\n',jornadas)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(info)
print(title)
print(tabla_dia,'\n')
print(legend)