# principle 1

# WRONG
try:
    average = sum(a_list) / len(a_list)
except ZeroDivisionError:
    average = 0

# Right
if len(a_list) > 0:
    averate - sum(a_list) / len(a_list)
else:
    average = 0
    
