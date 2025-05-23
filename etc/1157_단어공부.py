from collections import defaultdict

n = input()
input_str = n.lower()

def count(str):
    letter_dict = defaultdict(int)
    for char in str:
        letter_dict[char] += 1
    max_letter = ''
    max_occur = -99
    for key in letter_dict:
        if letter_dict[key] > max_occur:
            max_occur = letter_dict[key]
            max_letter = key
    count = 0
    for key in letter_dict:
        if letter_dict[key] == max_occur:
            count += 1
    if count > 1:
        return '?'
    else:
        return max_letter.upper()

print (count(input_str))
