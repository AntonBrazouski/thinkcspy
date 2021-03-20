# counts + histogram


def countAll(astring):
    counts = {}
    for ch in astring:
        if ch not in counts:
            counts[ch] = 1
        else:
            counts[ch] = counts[ch] + 1
    return counts


def hist_letters(astring):
    '''
    create a histogram of the number of times each letter occurs (sort asc)
    '''

    adict = countAll(astring)
    # adict = {'a':1, 'b':4}
    print(adict)
    print(get_values(adict))

    xs = get_values(adict)
    main(xs)



import turtle

def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()               # start filling this shape
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 # stop filling this shape


def main(xs):
    # xs = [48, 117, 200, 240, 160, 260, 220]  # here is the data
    maxheight = max(xs)
    numbars = len(xs)
    border = 10

    wn = turtle.Screen()             # Set up the window and its attributes
    wn.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border)
    wn.bgcolor("lightgreen")

    tess = turtle.Turtle()           # create tess and set some attributes
    tess.color("blue")
    tess.fillcolor("red")
    tess.pensize(3)



    for a in xs:
        drawBar(tess, a)

    wn.exitonclick()

def get_values(adict):
    alist = []
    for k,v in adict.items():
        alist.append(v)
    return alist

mystr = 'hello'
hist_letters(mystr)
