import sys

def tree_pointer(length, array):

    array.sort()

    INF = float('inf')
    big_neg = -INF
    big_neg_element = []
    small_pos = INF
    small_pos_element = []

    for i in range(length-2):
        left = i + 1
        right = length - 1

        while left < right:
            three_sum = array[i] + array[left] + array[right]
            if three_sum == 0:
                return array[i], array[left], array[right]

            if three_sum < big_neg:
                left += 1
                continue
            elif three_sum > small_pos:
                right -= 1
                continue

            if three_sum < 0:
                big_neg = three_sum
                big_neg_element = [array[i], array[left], array[right]]
                left += 1

            elif three_sum > 0:
                small_pos = three_sum
                small_pos_element = [array[i], array[left], array[right]]
                right -= 1

    if big_neg + small_pos >= 0:
        return big_neg_element
    else:
        return small_pos_element

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().strip().split()))
print (*tree_pointer(n, arr))