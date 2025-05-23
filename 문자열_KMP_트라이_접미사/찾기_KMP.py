def indexing(p):
    n = len(p)
    index_array = [0] * n
    j = 0
    for i in range(1, n):
        while j>0 and p[i] != p[j]:
            j = index_array[j-1]
        if p[i] == p[j]:
            j += 1
        index_array[i] = j
    return index_array

def kmp_searching(t, p, index_array):
    cnt = 0
    pos = []
    n = len(t)
    m = len(p)
    j = 0
    for i in range(n):
        while j>0 and t[i] != p[j]:
            j = index_array[j-1]
        if t[i] == p[j]:
            j += 1
        if j == m:
            cnt += 1
            pos.append(i-m+2)
            j = index_array[j-1]
    return cnt, pos

t = input()
p = input()

count, position = (kmp_searching(t, p, indexing(p)))
print (count)
for num in position:
    print (num)