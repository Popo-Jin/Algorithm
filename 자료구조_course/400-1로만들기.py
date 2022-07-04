X = int(input())
List_X = [0]*(X+1)

List_X[1] = 0

for i in range(2, X):

    List_X[i] = List_X[i-1]+1

    if i%3 == 0:
        List_X[i] = min(List_X[i], List_X[i//3]+1)
    if i%2 == 0:
        List_X[i] = min(List_X[i], List_X[i//2]+1)

print(List_X[X])
