

def file_to_list(afile):
    fileref = open(afile, 'r')
    blist = []
    # atuple = (0,0)
    for aline in fileref:
        alist = aline.split()
        blist.append(alist)
    fileref.close()

    return blist

def min_list(alist):
    min = alist[0]
    for item in alist:
        if item < min:
            min = item

    return min

def max_list(alist):
    max = alist[0]
    for item in alist:
        if item > max:
            max = item

    return max


def calc_minimax(alist):
    min = 0
    max = 0
    blist = alist[1:]
    name = alist[0]
    min = min_list(blist)
    max = max_list(blist)
    atuple = (name, min, max)

    return atuple

def process_lines():
    blist = []
    file = 'studentdata.txt'
    alist = file_to_list(file)
    for item in alist:
        aline = calc_minimax(item)
        blist.append(aline)
    
    return blist

def nice_print():
    lines = process_lines()
    for item in lines:
        print(f"{item[0].upper()} \t min score = {item[1]} \t max score= {item[2]} ")

print(nice_print())
