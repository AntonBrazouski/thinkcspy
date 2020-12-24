scores = [85, 95, 70]
result = ''
for score in scores:
    result = result + str(score) + ','

print("The scores are " + result)


scores = [85, 95, 70]
result = ''
for score in scores:
    if score == scores[len(scores) - 1]:
        result =  result + 'and ' + str(score) + '.'
    else:
        result = result + str(score) + ','

print("The scores are " + result)
