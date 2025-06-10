import sys

def change(n):
    coins = [2, 5]
    dp_lst = [-1] * (n+1)
    for coin in coins:
        if n>=coin:
            dp_lst[coin] = 1
        for i in range(n+1):
            if i >= coin and dp_lst[i-coin] != -1:
                dp_lst[i] = dp_lst[i-coin]+1
    return dp_lst[-1]

input = sys.stdin.readline
n = int(input())

print (change(n))