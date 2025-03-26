from collections import defaultdict

n = int(input())
input_lst = []
for i in range(n):
    string = input()
    input_lst.append(string)

def count(lst):
    answer_lst = []
    for string in lst:
        letter_dict = defaultdict(int)
        for letter in string.replace(' ', ''):
            letter_dict[letter] += 1
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
            answer_lst.append('?')
        else:
            answer_lst.append(max_letter)
    return answer_lst

answer = (count(input_lst))
for char in answer:
    print (char)