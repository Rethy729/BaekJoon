def checker(word_lst):
    cnt = 0
    for word in word_lst:
        letters = []
        for letter in word:
            if letter in letters and letters[-1] != letter:
                break
            else:
                letters.append(letter)
        if len(letters) == len(word):
            cnt += 1
    return cnt

n = int(input())
words = []
for _ in range(n):
    m = input()
    words.append(m)
print (checker(words))

