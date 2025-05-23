import sys
import heapq

def grid_to_graph(n, m, grid):
    graph = [[] for _ in range(n * m + 1)] #graph의 index는 1-based / (1,1)에 해당하는 node는 1이고, (n, m)에 해당하는 node는 nm+1이다
    for i in range(n):
        for j in range(m):
            if i != n-1:
                if grid[i][j] == '1' and grid[i+1][j] == '1':
                    graph[i*m + j + 1].append((i+1)*m + j + 1)
                    graph[(i+1)*m + j + 1].append(i*m + j + 1)
            if j != m-1:
                if grid[i][j] == '1' and grid[i][j+1] == '1':
                    graph[i*m + j + 1].append(i*m + j + 2)
                    graph[i*m + j + 2].append(i*m + j + 1)
    return graph

def dij (n, m, graph):
    distance = [float('inf')] * (n * m + 1)
    distance[1] = 0
    dij_queue = []
    heapq.heappush(dij_queue, (distance[1], 1))
    while dij_queue:
        dist, curr_node = heapq.heappop(dij_queue)
        if distance[curr_node] < dist:
            continue
        for next_node in graph[curr_node]:
            new_dist = dist + 1
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heapq.heappush(dij_queue, (new_dist, next_node))
    return distance[-1]

input = sys.stdin.readline
n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(input().strip())
graph = (grid_to_graph(n, m, grid))
print (dij(n, m, graph) + 1)