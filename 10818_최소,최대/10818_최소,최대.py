n = int(input())
m = list(map(int, input().split()))

max = -99999999
min = 99999999

for num in m:
    if num > max:
        max = num
    if num < min:
        min = num

print(min, end = ' ')
print(max, end = '')

#O(n)