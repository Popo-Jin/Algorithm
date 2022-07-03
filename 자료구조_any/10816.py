'''
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10
'''
first = int(input())
first_card = [0 for _ in range(first)]
first_card = list(map(int, input().split()))
second = int(input())
second_card = [0 for _ in range(second)]
second_card = list(map(int, input().split()))
print(first_card)
print(second_card)
# card = dict(first_card)
# print(card)