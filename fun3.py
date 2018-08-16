def draw_1d(line, row):
    print(("*"*row + "\n")*line)


def draw_2d(line, row, simbol):
    print((simbol*row + "\n")*line)

def special_draw_2d(line, row, border, fill):
    print(border*row)
    row -= 2
    line -= 2
    i = line
    while i > 0:
        print(border + fill*row + border)
        i -= 1
    print(border*(row+2))
    
special_draw_2d(7,24,"8",".")

