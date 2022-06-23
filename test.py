def solution(new_id):
    new_id = new_id.lower()
    answer=""
    pre = ''
    for i in new_id:
        if i=='-' or i=='_' or i=='.' or i.isdigit() or i.isalpha():
            answer += i
    
    print(answer)


solution("...!@BaT#*..y..abcdefghijklm")

# def solution(lottos, win_nums):
#     cnt = 0
#     zero = 0

#     for i in lottos:
#         if i in win_nums:
#             cnt += 1
#         if i == 0:
#             zero += 1
#     # answer = []
#     # return answer
    
#     return cnt, zero

# lottos = [6, 44, 2, 18, 40, 39]
# win_nums = [2, 4, 16, 19, 26, 39]

# print(solution(lottos, win_nums))

# def solution(id_list, report, k):
#     # 계정별 신고한 계정 목록 딕셔너리 생성(id_dict)
#     # 계정별 신고당한 횟수 딕셔너리 생성(abuse_cnt)
#     id_dict = {id: [] for id in id_list}
#     abuse_cnt_dict = {cnt: 0 for cnt in id_list}

#     # 중복 없애기 ex)입출력 예#2
#     # new_report = [] 
#     # for i in report:
#     #     if i not in new_report:
#     #         new_report.append(i)
#     new_report = set(report)
#     print(new_report)
#     # 계정별 신고한 계정 딕셔너리 작성
#     # 계정별 신고당한 횟수 딕셔너리 작성
#     for i in new_report:
#         reporter, abuser = i.split()
#         id_dict[reporter].append(abuser)
#         abuse_cnt_dict[abuser] += 1
#     print(id_dict)
#     print(abuse_cnt_dict)
#     # 신고당한 횟수가 k 이상인 계정 찾기
#     find_abuser = []
#     for id in abuse_cnt_dict:
#         if abuse_cnt_dict[id] >= k:
#             find_abuser.append(id)

#     # 계정당 메일 발송해야하는 횟수 구하기
#     answer = []
#     for user in id_dict:
#         cnt = 0
#         for i in find_abuser:
#             if i in id_dict[user]:
#                 cnt += 1
#         answer.append(cnt)
#     return answer

# id_list = ["a","b","c","d","e"]
# report = ["a b","a c","b d","b c","b e","c e","d e","a b","b d"]
# # id_list = ['1','2','3','4','5']
# # report = ["1 2","2 3","1 3","1 2","2 4","3 5","2 5","3 5"]
# solution(id_list,report,2)

# from random import randint
# a = [0,1,2,3,4,5]
# b = []
# for _ in range(0,100):
#     b.append(f"{randint(0,5)} {randint(0,5)}") 
# print(b)
# arr = set(b)
# print(arr)
# id_dict = {id:[] for id in a}
# cnt = {cnt:[] for cnt in a}
# print(len(arr))
# print(arr.pop().split(" "))

# print(id_dict)
# print(cnt)
# print(reporter)
# print(a)
# for i in arr:
#     reporter, abuser = i.split()
#     id_dict[id].append(abuser)
    # cnt[abuser] += 1
# for i in range(0, len(arr)):
#     set_id, set_cnt = arr[i].split(" ")
# print(id_dict)


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