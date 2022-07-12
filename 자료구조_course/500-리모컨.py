'''
5457
3
6 7 8
'''

N = int(input()) #채널
M = int(input()) #고장
if M != 0:
    L = list(map(int,input().split()))

K = [0,1,2,3,4,5,6,7,8,9]


print(N, M, L)

channel = list(map(int, str(N)))
print(channel)
if channel[i+1] < 5:

