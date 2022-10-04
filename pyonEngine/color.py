#base
black = (0, 0, 0)
white = (255, 255, 255)
#main

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
#other

yellow = (255, 255, 0)
purple = (255, 0, 255)
cyan = (0, 255, 255)


def hexcol(hex):
    
    if not len(hex) == 6:
        _missing = 6 - len(hex)
        for i in range(_missing):
            hex = hex + "0"
    
    _hex = [str(int(hex[0:2], 16)), str(int(hex[2:4], 16)), str(int(hex[4:6], 16))]
    return ", ".join(_hex)
    