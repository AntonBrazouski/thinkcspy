import turtle

def drawLsystem(aTurtle, instructions, angle, distance):
    savedInfoList = []
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == '[':
            savedInfoList.append([aTurtle.heading(), aTurtle.xcor(), aTurtle.ycor()])
            print(savedInfoList)
        elif cmd == ']':
            newInfo = savedInfoList.pop()


def process_string(oldstr):
    newstr = ""
    for ch in oldstr:
        newstr = newstr + apply_rules(ch)

    return newstr


def apply_rules(inst):
    result = ""
    for item in inst:
        if item == 'H':
            result = 'HFX[+H][-H]'
        elif item == 'X':
            result = 'X[-FFF][+FFF]FX'

    return result


def createLSystem(numIters,axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = process_string(startString)
        startString = endString

    return endString


t = turtle.Turtle()
inst = createLSystem(2,'H')
# inst =  'X[-FFF][+FFF]FX'
# inst =  'HFX[+H][-H]'
wn = turtle.Screen()
drawLsystem(t, inst, 27.5, 15)
wn.exitonclick()
