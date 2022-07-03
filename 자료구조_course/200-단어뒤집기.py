T = int(input())
result = []
for _ in range(T):
    Sentence = input()
    Sentence2 = Sentence.split()
    for i in range(len(Sentence2)):
        Sentence2[i] = Sentence2[i][::-1]
        if i == len(Sentence2)-1:
            print(Sentence2[i])
        else:
            print(Sentence2[i], end=" ")

    


'''
2
I am happy today
We want to win the first prize
'''