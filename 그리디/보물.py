import sys

input = sys.stdin.readline
n = int(input())
a_lst = list(map(int, input().strip().split()))
b_lst = list(map(int, input().strip().split()))
a_lst.sort()
b_lst.sort(reverse=True)

dot_product = 0
for i in range(n):
    dot_product += a_lst[i] * b_lst[i]

print (dot_product)
