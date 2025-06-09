import heapq
import sys

def dij (v, start, graph):
    distance = [float('inf')] * (v+1)
    distance[start] = 0
    dij_queue = []
    heapq.heappush(dij_queue, (distance[start], start))

    while dij_queue:
        dist, curr_node = heapq.heappop(dij_queue)

        if distance[curr_node] < dist:
            continue

        for next_node, weight in graph[curr_node]:
            new_dist = dist + weight
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heapq.heappush(dij_queue, (new_dist, next_node))
    return distance[1:]

input = sys.stdin.readline
v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    node_1, node_2, w = map(int, input().split())
    graph[node_1].append((node_2, w))  # 인접 리스트로 저장

distance_lst = dij(v, start, graph)
for dist in distance_lst:
    print (dist if dist != float('inf') else "INF")