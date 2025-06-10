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

n = int(input())
l = input()

cut_off = indexing(l)[-1]
print (n - cut_off)