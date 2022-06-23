from collections import deque

def bfs(graph, node): # 인접한 노드부터 탐색 -> 큐, 파이썬 특성상 덱 사용
    visited = [] # 방문한 노드를 담을 리스트
    not_visited = deque([node]) # 방문하지 않은 노드를 담을 덱
    while not_visited: # 방문하지 않은 노드가 있으면
        node = not_visited.popleft() # 먼저 들어간 노드를 뺌
        if node not in visited: # 방문하지 않은 노드가 방문한 리스트에 없으면
            visited.append(node) # 방문한 리스트에 넣고
            not_visited.extend(graph[node]) # 방문하지 않은 인접 노드를 graph에 추가
            print(not_visited)
    return visited # 더이상 방문하지 않은 노드가 없으면 방문한 리스트를 리턴

def dfs(graph, node): # 가장 나중에 들어간 노드부터 탐색 -> 스택 사용
    not_visited, visited = [], [] # 덱이 아닌 스택을 사용할거라 동일하게 선언
    not_visited.append(node)
    while not_visited:
        node = not_visited.pop()
        if node not in visited:
            visited.append(node)
            not_visited.extend(graph[node])

    return visited


graph = dict()
 
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

print(bfs(graph, 'A'))
# print(dfs(graph, 'A'))
