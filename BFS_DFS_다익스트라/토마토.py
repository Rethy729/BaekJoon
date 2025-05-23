import sys
import collections

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(grid, n, m):
    queue = collections.deque()
    for y in range(m):
        for x in range(n):
            if grid[y][x] == 1:
                queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < n and 0 <= new_y < m and grid[new_y][new_x] == 0:
                grid[new_y][new_x] = grid[y][x] + 1
                queue.append((new_x, new_y))
    return grid

def result (grid, n, m):
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                return -1
    passed_day = -1
    for i in range(m):
        for j in range(n):
            if grid[i][j] > passed_day:
                passed_day = grid[i][j]
    return passed_day-1

input = sys.stdin.readline
n, m = map(int, input().split())
grid = []
for _ in range(m):
    temp = input()
    grid.append(list(map(int, temp.strip().split(' '))))

new_grid = (bfs(grid, n, m))
print (result(new_grid, n, m))