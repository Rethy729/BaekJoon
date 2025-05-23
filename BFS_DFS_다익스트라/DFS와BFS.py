import collections


def dfs(v, start, graph):
    deq_dfs = collections.deque()
    visit = [False] * (v + 1)
    deq_dfs.append(start)

    order = []
    while deq_dfs:
        curr_node = deq_dfs.pop()

        temp_lst = graph[curr_node]  # 방문할 수 있는 node중 작은 것 부터 방문해야 하므로 따로 sort하여 처리
        temp_lst.sort(reverse=True)  # LIFO 임으로 역으로 정렬

        if not visit[curr_node]:               # 현재 뽑은 node가 non visit 상태이면
            visit[curr_node] = True            # 방문 처리 하고
            for next_node in temp_lst:         # 현재 node와 연결된 next node를 deque에 삽입
                if not visit[next_node]:       # 연결된 next node 또한 non visit 상태여야 함
                    deq_dfs.append(next_node)
                else:
                    continue
            order.append(curr_node)
    return order


def bfs(v, start, graph):
    deq_bfs = collections.deque()
    visit = [False] * (v + 1)
    deq_bfs.append(start)

    order = []
    while deq_bfs:
        curr_node = deq_bfs.popleft()

        temp_lst = graph[curr_node]  # 방문할 수 있는 node중 작은 것 부터 방문해야 하므로 따로 sort하여 처리
        temp_lst.sort()

        if not visit[curr_node]:
            visit[curr_node] = True
            for next_node in temp_lst:
                if not visit[next_node]:
                    deq_bfs.append(next_node)
                else:
                    continue
            order.append(curr_node)
    return order


v, e, start = map(int, input().strip().split(' '))
graph = collections.defaultdict(list)
for _ in range(e):
    v_1, v_2 = map(int, input().strip().split(' '))
    if v_2 not in graph[v_1]:
        graph[v_1].append(v_2)
        graph[v_2].append(v_1)

print(*dfs(v, start, graph))
print(*bfs(v, start, graph))
