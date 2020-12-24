import string


test_string = "Assign to a variable in your program a triple-quoted \
 string that contains your favorite paragraph of text - perhaps a poem,\
  a speech, instructions to bake a cake, some inspirational verses, etc."

alphabetic_char_count = 0
e_count = 0
e_percent = 0

for c in test_string:
    if c in string.ascii_lowercase or c in string.ascii_uppercase:
        alphabetic_char_count += 1
    if c == 'e' or c == 'E':
        e_count += 1

e_percent =  round((e_count / len(test_string) * 100 ),2)



result = f"Your text contains {alphabetic_char_count} alphabetic characters, \
 of which {e_count} ({e_percent}%) are 'e' ."

print(result)
