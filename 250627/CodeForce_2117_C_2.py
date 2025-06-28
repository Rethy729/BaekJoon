import sys
from collections import Counter

def partition(array):

    array.reverse()
    total_counter = Counter(array)
    current_counter = Counter()
    partition_cnt = 0

    while len(total_counter) != 0:
        for num in array:
            current_counter[num] += 1
            total_counter[num] -= 1

            if len(total_counter) == len(current_counter):
                current_counter = Counter()
                total_counter += Counter()
                partition_cnt += 1

    return partition_cnt

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    length = int(input())
    array = list(map(int, input().strip().split()))
    print(partition(array))