num = list(map(int, input().split()))

listen = []
see = []
for _ in range(num[0]):
    listen.append(input())
for _ in range(num[1]):
    see.append(input())

listen_set = set(listen)
see_set = set(see)
answer = list(listen_set&see_set)
answer.sort()
print (len(answer))
for element in answer:
    print (element)