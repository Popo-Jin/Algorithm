n = [int(input()) for _ in range(9)]

total = sum(n)

for i in range(len(n)):
    for j in range(i+1, len(n)):
            tmp = total - (n[i] + n[j])
            num1, num2 = n[i], n[j]
            if tmp == 100:
                n.remove(num1)
                n.remove(num2)
                n.sort()

                for i in range(len(n)):
                    print(n[i])
                exit()







