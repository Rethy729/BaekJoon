import sys

def tape_amount(n, m, leak_lst):
    covered = [False] * (max(leak_lst)+1)
    tape_count = 0
    for i in range(n):
        if covered[leak_lst[i]]:
            continue
        else:
            tape_count += 1
            for leak in leak_lst[i+1:]:
                if leak-leak_lst[i] < m:
                    covered[leak] = True
    return tape_count

input = sys.stdin.readline
n, m = map(int, input().strip().split())
leak_lst = list(map(int, input().strip().split()))
leak_lst.sort()
print (tape_amount(n, m, leak_lst))