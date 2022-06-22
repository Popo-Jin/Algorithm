'''
4 6
101111
101010
101011
111011
'''

from collections import deque


n,m = map(int, input().split())
maze = [[0 for _ in range(m)]for _ in range(n)]
dis = [[0 for _ in range(m)]for _ in range(n)]
for i in range(n):
    a = input()
    maze[i] = list(map(int, a))
dx = [-1,0,1,0]
dy = [0,1,0,-1]
not_visited = deque()

def bfs(maze, start_x, start_y):
    visited = [[False for _ in range(m)]for _ in range(n)]
    visited[start_x][start_y] = True
    dis[0][0] = 1
    not_visited.append([start_x, start_y])
    while not_visited:
        x, y = not_visited.popleft()    
        for i in range(4):
            new_x = x+dx[i]
            new_y = y+dy[i]
            if 0 <= new_x < n and 0 <= new_y < m and visited[new_x][new_y] == False and maze[new_x][new_y] == 1:
                not_visited.append([new_x, new_y])
                visited[new_x][new_y] = True
                dis[new_x][new_y] += dis[x][y]+1
                if new_x == n-1 and new_y == m-1:
                    return dis[n-1][m-1]

print(bfs(maze, 0, 0))