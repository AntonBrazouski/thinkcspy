afile = 'studentdata.txt'
with open(afile) as af:
    for line in af:
        data = line.split()
        if len(data) > 7:
            print(data[0])
