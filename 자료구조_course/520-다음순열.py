'''
4
1 2 3 4
'''

n = int(input())

m = list(map(int, input().split()))

for i in range(n-1, 0, -1):
    if m[i-1] < m[i]:
        for j in range(n-1, 0, -1):
            if m[i-1] < m[j]:
                m[i-1], m[j] = m[j], m[i-1]
                m = m[:i] + sorted(m[i:])
                print(*m)
                exit()

print(-1)
