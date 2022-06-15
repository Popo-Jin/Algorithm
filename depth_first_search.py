def dfs(graph, node):
    not_visited, visited = [], []
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

print(dfs(graph, 'A'))