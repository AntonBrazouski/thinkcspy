from test import assertEqual

def calc_sum(alist):
    sum = 0
    for i in range(len(alist)):
        if i > 0:
            sum += int(alist[i])
    return sum

def calc_avg(alist):
    return calc_sum(alist) / (len(alist) - 1)

with open('studentdata.txt', 'r') as data:
    alist = []
    blist = []
    for line in data:
        alist = line.split()
        print(alist)
        print(f"{alist[0]} - {calc_avg(alist):.2f} ")


testlist = ['joe',1, 2,3]
print(assertEqual(calc_avg(testlist), 2))
