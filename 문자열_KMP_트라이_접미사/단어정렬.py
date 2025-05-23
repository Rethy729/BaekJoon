def sorting(word_lst):
    set_a = set(word_lst)
    non_repeat_lst = list(set_a)

    non_repeat_lst.sort(key = lambda word:(len(word), word))
    return non_repeat_lst

n = int(input())
words = []
for _ in range(n):
    m = input()
    words.append(m)

sorted_words = sorting(words)
for word in sorted_words:
    print(word)