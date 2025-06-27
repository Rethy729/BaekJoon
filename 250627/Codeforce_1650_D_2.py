import sys

def twist(length, array):
    twist_lst = [0] * (length)
    temp_num = length

    while len(array) != 1:
        if array[-1] == temp_num:
            array.pop()
            temp_num -= 1
            continue

        for i in range(len(array)):
            if array[i] == temp_num:
                twist_lst[temp_num-1] = i+1
                array = array[i+1:] + array[:i]
                temp_num -= 1
                break
    return twist_lst


input = sys.stdin.readline
n = int(input())
for _ in range(n):
    length = int(input())
    array = list(map(int, input().strip().split()))
    print(*twist(length, array))
