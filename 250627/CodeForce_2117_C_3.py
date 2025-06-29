import sys

def partition(length, array):
    cur = set()
    seen = set()
    partition_cnt = 0

    for i in range(length):
        cur.add(array[i])
        seen.add(array[i])
        if len(cur) == len(seen):
            cur.clear()
            partition_cnt += 1

    return partition_cnt

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    length = int(input())
    array = list(map(int, input().strip().split()))
    print(partition(length, array))