"""This is the entry point of the program."""


def create_box(height, width, character):
    box = ''
    for i in range(height):
        box_width = ''
        for j in range(width):
            box_width += character
        box_width += '\n'
        box += box_width
    return box


def create_special_box(height, width, character):
    topbot = width*character + '\n'
    middle = ''
    for i in range(height-2):
        box_width = character
        for j in range(width-2):
            box_width += ' '
        box_width += character + '\n'
        middle += box_width
    
    finalbox = topbot + middle + topbot
    
    return finalbox 
    


if __name__ == '__main__':
    create_box(3, 4, '*')
