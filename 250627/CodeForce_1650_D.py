import sys

def twist(length, array):
    order_lst = [0] * (length)
    twist_lst = [0] * (length)
    for i in range(length):
        order_lst[array[i]-1] = i + 1
    #print (order_lst)

    for i in range(length, 0, -1): #i는 6부터 1까지
        while order_lst[i-1] != i:
            for j in range(i):
                order_lst[j] = order_lst[j]-1
                if order_lst[j] == 0:
                    order_lst[j] = i
            twist_lst[i-1] += 1
        #print (order_lst)

    return twist_lst

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    length = int(input())
    array = list(map(int, input().strip().split()))
    print(*twist(length, array))