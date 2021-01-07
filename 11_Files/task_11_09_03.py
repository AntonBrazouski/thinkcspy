

def file_to_list(afile):
    fileref = open(afile, 'r')
    blist = []
    # atuple = (0,0)
    for aline in fileref:
        alist = aline.split()
        blist.append(alist)
    fileref.close()
    print(blist)
    return blist

def min_list(alist):
    if alist == []:
        return None
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

#
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

print(process_lines())
