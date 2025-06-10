import sys

def scheduling(n, meeting):
    current_meeting = meeting[0]
    meeting_cnt = 1
    for i in range(1, n):
        if current_meeting[1] <= meeting[i][0]:
            meeting_cnt += 1
            current_meeting = meeting[i]
    return meeting_cnt

input = sys.stdin.readline
n = int(input())
meeting = []
for _ in range(n):
    meeting.append(list(map(int, input().strip().split())))
meeting = sorted(meeting, key=lambda x: (x[1], x[0]))
print (scheduling(n, meeting))