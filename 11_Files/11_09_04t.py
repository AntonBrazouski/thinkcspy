import turtle

def interpret():
    file = 'labdata.txt'
    items = []
    with open(file, 'r') as f:
        for line in f:
            (x, y) =  line.split()
            items.append((int(x), int(y)))
    return items



def draw_cords(alist):
    x_max = max(get_x(alist))
    y_max = max(get_y(alist))

    wn = turtle.Screen()
    wn.setworldcoordinates(0,0,x_max + 50,y_max + 50)
    alex = turtle.Turtle()
    for cords in alist:
        alex.up()
        alex.goto(cords[0],cords[1])
        alex.stamp()
    wn.exitonclick()

def calc_sum(alist):
    sum = 0
    for i in range(len(alist)):
        sum += int(alist[i])
    return sum


def calc_mean(alist):
    return calc_sum(alist) / (len(alist))


def get_x(alist):
    blist = []
    for i in range(len(alist)):
        blist.append(alist[i][0])
    return blist


def get_y(alist):
    blist = []
    for i in range(len(alist)):
        blist.append(alist[i][1])
    return blist


# def plotRegression(alist):
#     print(alist)
#     mx = calc_mean(get_x(alist))
#     my = calc_mean(get_y(alist))
#     n = len(alist)
#     return (mx,my,n)

def calc_regression(alist):
    x_list = get_x(alist)
    y_list = get_y(alist)
    n = len(alist)
    x_mean = calc_mean(get_x(alist))
    y_mean = calc_mean(get_y(alist))

    blist = []
    m = 0
    y = 0

    m1 = 0
    for i in range(len(alist)):
        m1 = m1 + alist[i][0] * alist[i][1]

    m1 = m1 - n * x_mean * y_mean

    m2 = 0
    for i in range(len(alist)):
        m2 = m2 + alist[i][0]**2
    m2 = m2 - n * (x_mean ** 2)

    m = 0
    m = m1 / m2
    # print(f"m1={m1} m2={m2} m= {m}")

    for i in range(len(alist)):
        x = alist[i][0]
        y = int(y_mean + m * (x + x_mean))
        # print(f" x= {x} x_mean={x_mean} m={m} (m*(x+x_mean)={m*(x+x_mean)}")
        blist.append((x, y))
    return blist

alist = interpret()
print(alist)
blist=calc_regression(alist)
# draw_cords(alist)
draw_cords(blist)
# print(calc_sum(alist[1]))
#print(get_y([(1,2),(3,4)]))
#print(plotRegression(alist))
# print(calc_mean([1,2,3]))

#           TODO
# unite draw cords with draw line (regression)
# fillcolor("red")
# wn.bgcolor("lightgreen")
# tess.pensize(3)
#  write draw_line funciton
