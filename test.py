from random import randint

a = [0,1,2,3,4,5]
b = []
for _ in range(0,100):
    b.append(f"{randint(0,5)} {randint(0,5)}") 
print(b)
arr = set(b)
print(arr)
id_dict = {id:[] for id in a}
cnt = {cnt:[] for cnt in a}
# print(len(arr))
# print(arr.pop().split(" "))
a1, a2 = arr.pop().split(" ")
print(a1,"and",a2)
# for i in range(0, len(arr)):
#     set_id, set_cnt = arr[i].split(" ")
print(id_dict)


# from collections import deque
# import time

# start_time = time.time() #시작 시간
# ###
# # a = []
# a = deque()
# b = []
# c = []
# for num in range(0,10000000):
#     # a.append(num)
#     b.append(num)
# while a:
#     num = b.pop()
#     # num = a.popleft()
#     # num = a.pop()
#     c.append(num)
# ###
# end_time = time.time() #종료 시간

# print("알고리즘 수행 시간 : ", end_time - start_time)


# def while_check(data):
#     i = 0
#     while data:
#         print(i,"번")
#         if data[i] == 1:
#             return data[i]
#         else:
#             i += 1
        
# data = [4,5,1,6,7]
# print(while_check(data))                     -----------> while 문 내부에 if문에서 return하면 while문도 종료

# def none_check():
#     a = None
#     b = 1
#     if a:
#         print("None is value")
#     elif b:
#         print("None is not value")            ---------> None은 값이 없음


# none_check()

# def third_none_check(a,b):
#     if a == b == None:
#         print("a, b = None")
#     else:
#         print("a, b != None")

# third_none_check(None,None)                     ---------> a == b == None은 a,b 둘다 None이여야만 성립


# if not True:
#     print("1")
# else:
#     print("2")


# graph = dict()
 
# graph['A'] = ['B', 'C']
# graph['B'] = ['A', 'D']
# graph['C'] = ['A', 'G']

# node = 'A'

# a = ['banana']
# b = {1,2,3}
# x = []

# # x.append(graph['A'])
# x.append(b)
# print(x)