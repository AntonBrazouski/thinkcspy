import turtle

def readfile():
    alist = []
    file = 'mystery.txt'
    with open(file, 'r') as f:
        for aline in f:
            values = aline.split()
            alist.append(values)
    return alist

def draw_picture(alist):
    wn = turtle.Screen()
    t = turtle.Turtle()
    for point in alist:
        if point == ['UP']:
            turtle.up()
        elif point == ['DOWN']:
            turtle.down()
        else:
            turtle.goto(int(point[0]), int(point[1]))
            # print(point)

    wn.exitonclick()

draw_picture(readfile())
