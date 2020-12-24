def replace(s, old, new):
    result = ""
    result = s.split(new)
    result = new.join(result)

    return result

print(replace("hi man", "hi", "yo!"))
