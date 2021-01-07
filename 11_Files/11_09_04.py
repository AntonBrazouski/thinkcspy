

def file_to_list(afile):
    fileref = open(file, 'r')
    blist = []
    # atuple = (0,0)
    for aline in fileref:
        alist = aline.split()
        atuple = alist[0], alist[1]
        blist.append(atuple)
    print(blist)
    fileref.close()


file = 'labdata.txt'
file_to_list(file)
