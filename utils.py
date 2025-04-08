import os

def get_rgb(number: int) -> tuple:

    # test this more - why should numerator be -1ed

    # return type tuple with variable length
    # cell colour should depend on abilities and not be random
    """
    Convert a two-digit number(0-99) to rgb(0-255) values
    """
    combination = ( ((256**3)-1) / (100-1) ) * (number)
    
    rgb = []
    
    for i in range(2, 0-1, -1):
        rgb.append(int(combination/256**i))
        combination = combination%256**i
    
    return rgb

def clrscr():
    os.system("cls")