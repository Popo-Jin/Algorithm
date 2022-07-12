n = int(input())
m = [[0 for _ in range(n)] for _ in range(n)]
x = [[0 for _ in range(n)] for _ in range(n)]
y = [[0 for _ in range(n)] for _ in range(n)]

for i in range(len(m)):
    m[i] = list(map(str, input()))

tmp = m
num = [0,0,0,0]
num2 = [0,0,0,0]
for i in range(len(tmp)):
    for j in range(len(tmp)):
        if tmp[i+1][j] == 'C':
            num[0] += 1
        elif tmp[i+1][j] == 'P':
            num[1] += 1
        elif tmp[i+1][j] == 'Z':
            num[2] += 1
        elif tmp[i+1][j] == 'Y':
            num[3] += 1
        
    x.append(max(num))
    num = [0,0,0,0]

for i in range(len(x)):
    print(x[i])