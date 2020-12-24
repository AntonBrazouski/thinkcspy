prefixes = "JKLMNOPQ"
suffix = "ack"

for p in prefixes:
    if p == 'Q' or p == 'O':
        suffix = 'u' + suffix
    else:
        
        suffix = "ack"
    print(p+suffix)
