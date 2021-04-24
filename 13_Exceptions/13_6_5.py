try:
    f = open("my_file.txt", "w")
    try:
        f.write("Writing some data to the file")
    finally:
        f.close()
except IOError:
    print("Error: my_file.txt does not exist or it can't be opened for output.")
