n, m = map(str, input().split())

def bin_to_ten(string):
    num = 0
    for i in range(len(string)):
        num += (2**i) * int(string[len(string)-1-i])
    return num

#O(n)

def ten_to_bin(num, lst):
    a = num // 2
    b = num % 2
    lst.append(b)
    if a == 0:
        return lst
    else:
        return ten_to_bin(a, lst)

#O(log2n)

answer = []
binary_num = (ten_to_bin(bin_to_ten(n)+bin_to_ten(m), answer))
binary_str = ''.join(map(str, binary_num[::-1]))
print (binary_str)

#총합 O(n)