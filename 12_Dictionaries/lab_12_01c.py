# print(countAll("banana"))

# {"a":3, "b":1, "n":2}

def countAll(astring):
    counts = {}
    for ch in astring:
        if ch not in counts:
            counts[ch] = 1
        else:
            counts[ch] = counts[ch] + 1
    return counts

def main():
    print(countAll("banana"))

if __name__ == '__main__':
    main()
