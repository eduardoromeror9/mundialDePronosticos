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
        Jornadas: 20
        Juegos: 60
        
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

tabla_dia.add_row([' Daniel',    '37-23', '-', ' 615 '])
tabla_dia.add_row([' Christian', '37-23', '-', ' 615 '])
tabla_dia.add_row([' CarlosJ',   '37-23', '-', ' 615 '])
tabla_dia.add_row([' Erycherd',  '36-24', '1', ' 600 '])
tabla_dia.add_row([' Eduardo',   '34-26', '3', ' 565 '])
tabla_dia.add_row([' Kleydi',    '34-26', '3', ' 565 '])
tabla_dia.add_row([' Steven',    '34-26', '3', ' 565 '])



print('\n',jornadas)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(info)
print(title)
print(tabla_dia,'\n')
print(legend)