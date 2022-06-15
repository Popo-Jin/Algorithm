
from collections import deque


def bfs(graph, node, visited): #너비탐색을 진행할 graph, 시작노드 node, 방문한 노드 visited
    queue = deque([node]) # 시작노드를 queue에 넣음
    visited[node] = True # 시작노드를 방문처리

    while queue: 
        v = queue.popleft() # 선입선출
        print(v, end=' ') # 탐색 순서 출력
        for i in graph[v]: 
            if visited[i] == False: 
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3],
    [1, 8],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7, 8],
    [6, 8],
    [2, 6, 7]
]

visited = [False]*9

bfs(graph, 1, visited)