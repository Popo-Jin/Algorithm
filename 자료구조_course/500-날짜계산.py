E, S, M = map(int, input().split())

n = [15, 28, 19]

while True:
    if E == S == M:
        print(E)
        break
    else:
        if min(E, S, M) == E:
            E += n[0]
        elif min(E, S, M) == S:
            S += n[1]
        elif min(E, S, M) == M:
            M += n[2]
