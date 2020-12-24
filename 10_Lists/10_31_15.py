def set_rules(s):
    result = ''
    if 's' == 'H':
        result = 'HFX[+H][-H]'
    if 's' == 'X':
        result = 'X[-FFF][+FFF]FX'

def process_rules(s):
    result = ""
    for item in s:
        if item == 'F':
            result = 'forward'
