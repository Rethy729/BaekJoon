import sys

def sensor(n, k, coordinate):
    coordinate.sort()
    distance = []
    for i in range(n-1):
        distance.append(coordinate[i+1] - coordinate[i])
    distance.sort(reverse=True)
    return sum(distance[k-1:])

input = sys.stdin.readline
n = int(input())
k = int(input())
coordinate = list(map(int, input().strip().split()))

print (sensor(n, k, coordinate))