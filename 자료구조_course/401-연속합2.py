'''
10
10 -4 3 1 5 6 -35 12 21 -1
54
'''

n = int(input())
m = [0]*n
m = list(map(int, input().split()))
f = []
g = []
check = 0
result = 0
result_no = 0
result_yes = 0
for i in range(len(m)):
    if m[i] >= 0:
        result += m[i]
    else:
        if result != 0:
            f.append(result)
            result = 0

for i in range(len(f)):
    if f[i] >= 0:
        result_no += f[i]
        result_yes += f[i]
    else:
        g.append(result_no)
        result_no = 0
        if check == 0:
            check = 1
        else:
            g.append(result_yes)
            result_yes = 0
            check = 0

for i in range(len(g)):
	result = max(g[i], result)

print(result)