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
        Jornadas: 16
        Juegos: 48

        
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
"""

title = PrettyTable(['🔥🔥 Mundial de pronosticos 🔥🔥'])
tabla_dia = PrettyTable(['Players', 'G-P', 'DIF', 'PCT %'])

tabla_dia.add_row([' Daniel',    '31-17', '-', ' 645 '])
tabla_dia.add_row([' Christian', '31-17', '-', ' 645 '])
tabla_dia.add_row([' Erycherd',  '30-18', '1', ' 625 '])
tabla_dia.add_row([' CarlosJ',   '29-19', '2', ' 605 '])
tabla_dia.add_row([' Eduardo',   '27-21', '4', ' 565 '])
tabla_dia.add_row([' Kleydi',    '27-21', '4', ' 565 '])
tabla_dia.add_row([' Steven',    '24-24', '7', ' 500 '])



print('\n',jornadas)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(info)
print(title)
print(tabla_dia,'\n')
print(legend)