x,y,w,h = map(int, input().split())
height = h-y
weight = w-x
min = height
arr = [height, weight, x, y]
for i in arr:
    if min > i:
        min = i

print(min)
