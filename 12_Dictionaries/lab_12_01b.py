# def countA(text):
#     count = 0
#     for c in text:
#         if c == 'a':
#             count = count + 1
#     return count
#
# print(countA("banana"))
#

def countA(text):
    return text.count("a")

print(countA('bananamama'))
