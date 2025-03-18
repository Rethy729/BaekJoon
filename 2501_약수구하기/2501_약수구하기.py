n, k = map(int, input().split())

def yak_soo(n, k):
    yak_soo= []
    for i in range(1, int(n**(1/2))+1):
        if n%i == 0:
            if i == n/i:
                yak_soo.append(i)
            else:
                yak_soo.append(i)
                yak_soo.append(n/i)
    yak_soo.sort()
    if k > len(yak_soo):
        return 0
    else:
        return int(yak_soo[k-1])

print (yak_soo(n, k))

# 시간복잡도 O(n^(1/2))