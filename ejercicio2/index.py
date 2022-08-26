# import time (this import the complete module)

from time import localtime

hour24 = localtime().tm_hour
minutes = localtime().tm_min

if hour24 >= 19:
    print("Es hora de ir a casa")

if hour24 < 19:
    print("Tiempo restante para ir a casa: {} horas y {} minutos".format(18 - hour24, 59 - minutes))

