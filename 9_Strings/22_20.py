def remove_dumps(astring):
    result = ''
    for ch in astring:
        if ch not in result:
            result += ch

    return result

print(remove_dumps('catacomba!'))
print(remove_dumps('MMA FIGHTER'))
print(remove_dumps('auch!'))
print(remove_dumps(''))
