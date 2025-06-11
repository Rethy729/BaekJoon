import sys
import heapq

def classrooms(n, lectures):
    classroom = []
    heapq.heappush(classroom, lectures[0][1])
    for i in range(1, n):
        if lectures[i][0] < classroom[0]:
            heapq.heappush(classroom, lectures[i][1])
        else:
            heapq.heappop(classroom)
            heapq.heappush(classroom, lectures[i][1])
    return len(classroom)

input = sys.stdin.readline
n = int(input())
lectures = []
for _ in range(n):
    lectures.append(list(map(int, input().strip().split())))
lectures.sort()

print (classrooms(n, lectures))