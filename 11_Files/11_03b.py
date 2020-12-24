# make a file error

fileref = open("qbdata.txt", "r")
fileref.close()
f = fileref # let's make an error by reffering to the closed file
print(f.encoding) # no error ?
