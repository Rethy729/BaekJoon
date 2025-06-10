import sys

def rope_greedy(n, ropes_lst):
    max_weight = 0
    for i in range(n):
        if ropes_lst[i] * (n-i) > max_weight:
            max_weight = ropes_lst[i] * (n-i)
    return max_weight

input = sys.stdin.readline
n = int(input())
ropes = []
for _ in range(n):
    ropes.append(int(input()))
ropes.sort()
print (rope_greedy(n, ropes))