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