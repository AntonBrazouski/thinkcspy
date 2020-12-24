## and write your own applyRules function to implement this L-system

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
            aTurtle.setheading(newInfo[0])
            aTurtle.setposition(newInfo[1], newInfo[2])

def applyRules(lhch):
    rhstr = ""
    if lhch == 'F':
        rhstr = 'FF-B['   # Rule 1
    elif lhch == 'B':
        rhstr = '+]FBF'  # Rule 2
    else:
        rhstr = lhch    # no rules apply so keep the character

    return rhstr

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)

    return newstr


def createLSystem(numIters,axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString

    return endString


t = turtle.Turtle()
inst = createLSystem( 5,'F')
t.setposition(0, -200)
t.left(90)
drawLsystem(t, inst, 15, 5)
