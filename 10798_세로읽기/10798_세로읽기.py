input_lst = []
for _ in range(5):
    input_lst.append(input())

def saero_read(lst):
    saero_read = ''
    max_len = len(max(lst, key = len))
    for i in range(max_len):
        for j in range(5):
            if len(lst[j]) <= i:
                continue
            else:
                saero_read += lst[j][i]
    return (saero_read)
print (saero_read(input_lst))