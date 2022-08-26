from time import localtime

hour24 = localtime().tm_hour

if hour24 >= 19:
    print("Es hora de ir a casa")

if hour24 < 19:
    print("Tiempo restante para ir a casa:", 19 - hour24)

