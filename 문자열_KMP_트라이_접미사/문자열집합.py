def check (set_word_lst, check_word_lst):
    cnt = 0
    for word in check_word_lst:
        if word in set_word_lst:
            cnt += 1
    return cnt

n, m= map(int,input().split(' '))
set_words = []
check_words = []
for _ in range(n):
    word = input()
    set_words.append(word)
for _ in range(m):
    word = input()
    check_words.append(word)

print (check(set_words, check_words))



