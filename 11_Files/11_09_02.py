def count_stats(aline):
    data = aline.split()
    print(data)
    print(len(data))
    array_data = []
    for i in range(1, len(data), 1):
        array_data.append(int(data[i]))
    print(array_data)
    count = len(array_data)

    sum = 0
    for item in array_data:
        sum += item
    if count == 0:
        return None
    else:
        return sum / count

af = open('studentdata.txt', "r")
for line in af:
    print(line)
    line = af.readline()
    st = count_stats(line)
    print(f"{st}")
# print(line)
af.close()
