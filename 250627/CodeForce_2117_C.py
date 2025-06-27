import sys
from collections import defaultdict

def partition(length, array):

    cnt_dict = defaultdict(int)
    partition_cnt = 0

    start = True
    temp_cnt = []

    for n in array:
        cnt_dict[n] += 1

        if start:
            values = [v for v in cnt_dict.values()]
            for i in range(len(values), 0, -1):
                if min(values[:i]) >= 2:
                    partition_cnt += 1
                    for j, key in enumerate(cnt_dict):
                        if j >= i:
                            break
                        cnt_dict[key] -= 1
                    start = False
                    temp_cnt = [v for v in cnt_dict.values()]
                    break

        else:
            values = [v for v in cnt_dict.values()]
            values_n = values[:len(temp_cnt)]
            partition_add = False
            for i in range(len(temp_cnt)):
                if temp_cnt[i] < values_n[i] and values_n[i] % temp_cnt[i] == 0:
                    partition_add = True
                else:
                    partition_add = False
                    break
            if partition_add:
                partition_cnt += 1
                for i, key in enumerate(cnt_dict):
                    if i >= len(values_n):
                        break
                    cnt_dict[key] -= temp_cnt[i]
                temp_cnt = [v for v in cnt_dict.values()]
    return (partition_cnt + 1)

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    length = int(input())
    array = list(map(int, input().strip().split()))
    print(partition(length, array))