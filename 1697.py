from collections import deque



n, k = map(int, input().split())



def bfs(start):
    while queue:
        start = queue.popleft()
        if 0 > start and start > 1000000:
            continue
        for i in (start-1, start+1, start*2):
            if 0 <= i and i <= 1000000:
                queue.append(i)
                if dis[i] == 0:
                    dis[i] = dis[start]+1
                if i == k:
                    return dis[i]


if n == k:
    print(0)
elif n < k:
    queue = deque([n])
    dis = [0 for _ in range(0, 1000001)]
    print(bfs(queue))
else:
    print(n-k)




