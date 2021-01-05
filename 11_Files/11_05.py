# Alternate file reading methods

infile = open("qbdata.txt", "r")
aline = infile.readline()
print(aline)

infile = open("qbdata.txt", "r")
linelist = infile.readlines()
print(len(linelist))

print(linelist[0:4])

infile = open("qbdata.txt", "r")
filestring = infile.read()
print(len(filestring))

print(filestring[:256])
