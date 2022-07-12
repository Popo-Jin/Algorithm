'''
5457
3
6 7 8
'''

N = int(input()) #채널
M = int(input()) #고장
K = [0,1,2,3,4,5,6,7,8,9]

if M != 0:
    L = list(map(int,input().split())) #고장난 버튼
    for var in L:
        K.remove(var)

channel = list(map(int, str(N)))
check = [-2 for _ in range(len(channel))]
check2 = [-2 for _ in range(len(channel))]
for i in range(len(channel)):
    min_num = 9
    if channel[i] not in K:
        for j in range(len(K)):
            if min_num == abs(K[j]-channel[i]):
                if check[i] == 0:
                    check[i] = K[j]
                else:
                    check2[i] = K[j]
            min_num = min(min_num, abs(K[j]-channel[i]))
    else:
        check[i] = channel[i]

print(N, M, L, K)
print(channel)
print(check)
print(check2)
result = ''
result2 = ''
for var in channel:
    result += str(var)
for var in check:
    result2 += str(var)
if N == 100:
    print(0)
else:
    print(len(check)+abs(int(result)-int(result2)))







