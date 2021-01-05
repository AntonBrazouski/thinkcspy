# 11.4 Iterating over lines in a file

qbfile = open("qbdata.txt", "r")

for aline in qbfile:
    values = aline.split()
    print('QB', values[0], values[1], 'had a rating of ', values[10])

qbfile.close()
