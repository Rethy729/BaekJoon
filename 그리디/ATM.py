def atm(n, lst):

    lst.sort(reverse=True)
    sum_atm = 0
    for i in range(n):
        sum_atm += lst[i] * (i+1)
    return sum_atm

n = int(input())
m = list(map(int, input().strip().split()))
print (atm(n, m))