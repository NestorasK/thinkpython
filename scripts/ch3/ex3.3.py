# 1
def drawgrid(numCol):
    drawgrid_basic_part(numCol)
    drawgrid_basic_part(numCol)
    draw_line(numCol)

def draw_line(numCol):
    cat = ('+' + ' - '*4)# '+' + ' - '*4 +
    out = cat * numCol + '+'
    print(out)

def draw_vertical(numCol):
    cat = '|' + '   '*4
    out = cat*numCol + '|'
    print(out)

def draw_vertical_space(numCol):
    draw_vertical(numCol)
    draw_vertical(numCol)
    draw_vertical(numCol)
    draw_vertical(numCol)

def drawgrid_basic_part(numCol):
    draw_line(numCol)
    draw_vertical_space(numCol)


drawgrid(2)

# 2
print("Q2")
def drawgrid_4(numCol):
    drawgrid_basic_part(numCol)
    drawgrid_basic_part(numCol)
    drawgrid_basic_part(numCol)
    drawgrid_basic_part(numCol)
    draw_line(numCol)

drawgrid_4(4)
