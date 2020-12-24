def replace(s, old, new):
    s2 = ""
    ar = s.split(old)
    result = new.join(ar)

    return result

print(replace("hi man", "hi", "yo!"))
