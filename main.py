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
        Jornadas: 14
        Juegos: 42

        
        Carlos Jose cree
        que va a ganar
        pero ese no le gana
        ni a paquito
        jugando reloj

        Steven por PRIMERA VEZ
        en los 500 de promedio
            
"""

title = PrettyTable(['🔥🔥 Mundial de pronosticos 🔥🔥'])
tabla_dia = PrettyTable(['Players', 'G-P', 'DIF', 'PCT %'])

tabla_dia.add_row([' Daniel',      '27-15', '-', ' 640 '])
tabla_dia.add_row([' Christian',   '27-15', '-', ' 640 '])
tabla_dia.add_row([' Erycherd',    '26-16', '1', ' 620 '])
tabla_dia.add_row([' CarlosJ',     '26-16', '1', ' 620 '])
tabla_dia.add_row([' Eduardo',     '24-18', '3', ' 570 '])
tabla_dia.add_row([' Kleydi',      '23-19', '4', ' 545 '])
tabla_dia.add_row([' Steven',      '21-21', '6', ' 500 '])



print('\n',jornadas)
print('\n   ⚾⚾⚾⚾ Tabla del DIA ⚾⚾⚾⚾\n')
print(title)
print(tabla_dia,'\n')
print(legend)