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
        Jornadas: 15
        Juegos: 45

        
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

tabla_dia.add_row([' Daniel',    '30-15', '-', ' 665 '])
tabla_dia.add_row([' Christian', '30-15', '-', ' 665 '])
tabla_dia.add_row([' CarlosJ',   '28-17', '2', ' 620 '])
tabla_dia.add_row([' Erycherd',  '27-18', '3', ' 600 '])
tabla_dia.add_row([' Eduardo',   '25-20', '5', ' 555 '])
tabla_dia.add_row([' Kleydi',    '24-21', '6', ' 530 '])
tabla_dia.add_row([' Steven',    '23-22', '7', ' 510 '])



print('\n',jornadas)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(info)
print(title)
print(tabla_dia,'\n')
print(legend)