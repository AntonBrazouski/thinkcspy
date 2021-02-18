def interpret():
    file = 'labdata.txt'
    with open(file, 'r') as f:
        for line in f:
            (x, y) =  line.split()
            items.append(x, y)


def draw_cords(alist):
    wn = turtle.Screen()
    alex = turtle.Turtle()
    for cords in alist:
        alex.up()
        alex.goto(cords[0],cords[1])
        alex.stamp()
    wn.exitonclick()


def plotRegression():
    pass
