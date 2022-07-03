from multiprocessing.connection import answer_challenge


arr = [1,0,2,3,0,4,5]
answer_tmp = []
for num in arr:
    if num == 0:
        answer_tmp.append(num)
    answer_tmp.append(num)

answer = answer_tmp[:len(arr)]

print(answer_tmp)
print(answer)

for i in range(len(arr)):
    arr[i] = answer[i]

print(arr)