import sys

input = sys.stdin.readline
n = int(input())
database = []
for i in range(n):
    database.append([i] + input().strip().split())

database = sorted(database, key=lambda x: (int(x[1]), x[0]))
for data in database:
    print (data[1]+' '+data[2])