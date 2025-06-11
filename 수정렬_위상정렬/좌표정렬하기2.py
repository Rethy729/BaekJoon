import sys

input = sys.stdin.readline
n = int(input())
coordinates = []
for i in range(n):
    coordinates.append(list(map(int, input().strip().split())))

coordinates = sorted(coordinates, key=lambda x: (x[1], x[0]))
for point in coordinates:
    print (str(point[0]) + ' ' + str(point[1]))
