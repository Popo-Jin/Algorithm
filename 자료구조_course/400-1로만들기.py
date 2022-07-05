X = int(input())
List_X = [0]*1000000
cnt = 0
while List_X[1] == 0:

    if X%3 == 0:
        result = X//3
        if List_X[result] == 0:
            List_X[result] = 1
    elif X%2 == 0:
        result = X//2
        if List_X[result] == 0:
            List_X[result] = 1
    else:
        result = X-1
        if List_X[result] == 0:
            List_X[result] = 1

