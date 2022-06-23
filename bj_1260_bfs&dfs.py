'''
4 6
101111
101010
101011
111011
'''

from collections import deque


n, m = map(int, input().split())
maze = [[0 for _ in range(m)] for _ in range(n)]
count = [[0 for _ in range(m)] for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
for i in range(n):
    a = input()
    maze[i] = list(map(int, a))
queue = deque()

def bfs(maze, start_x, start_y):
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[start_x][start_y] = True
    queue.append([start_x, start_y])
    count[start_x][start_y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < m and 0 <= new_y < n and not visited[new_y][new_x]:
                if maze[new_y][new_x] == 1:
                    visited[new_y][new_x] = True
                    queue.append([new_x,new_y])
                    count[new_y][new_x] = count[y][x]+1
                    if new_y == m-1:
                        a = count[new_y][new_x]
                        queue.clear()
                        return a

print(bfs(maze, 0, 0))