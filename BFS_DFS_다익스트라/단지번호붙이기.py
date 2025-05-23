import sys
import collections

def grid_to_graph(n, grid):
    graph = [[] for _ in range(n * n + 1)] #graph의 index는 1-based / (1,1)에 해당하는 node는 1이고, (n, m)에 해당하는 node는 nm+1이다
    graph_zero_one = [False] * (n * n + 1) #집이 있는 위치만 나열한 list (0or1)

    for i in range(n):
        for j in range(n):
            if grid[i][j] == '1':
                graph_zero_one[i*n+ j + 1] = True
            if i != n-1:
                if grid[i][j] == '1' and grid[i+1][j] == '1':
                    graph[i*n+ j + 1].append((i+1)*n + j + 1)
                    graph[(i+1)*n + j + 1].append(i*n + j + 1)
            if j != n-1:
                if grid[i][j] == '1' and grid[i][j+1] == '1':
                    graph[i*n + j + 1].append(i*n + j + 2)
                    graph[i*n+ j + 2].append(i*n + j + 1)
    return graph, graph_zero_one

def counting_components(n, graph, graph_zero_one):
    deq_bfs = collections.deque()
    visit = [False] * (n * n + 1)
    components = []

    for i in range(1, n*n+1):
        component = []
        if not visit[i] and graph_zero_one[i]:
            deq_bfs.append(i)
            while deq_bfs:
                curr_node = deq_bfs.popleft()
                if not visit[curr_node]:
                    visit[curr_node] = True
                    for next_node in graph[curr_node]:
                        if not visit[next_node]:
                            deq_bfs.append(next_node)
                        else:
                            continue
                    component.append(curr_node)
        if component:
            components.append(component)
    return components

input = sys.stdin.readline
n = int(input())
grid = []
for _ in range(n):
    grid.append(input().strip())

graph, graph_zero_one = grid_to_graph(n, grid)
cc = counting_components(n, graph, graph_zero_one)
print (len(cc))
length = []
for danji in cc:
    length.append(len(danji))
length.sort()
for num in length:
    print (num)