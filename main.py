import time

start_time = time.time() #시작 시간
###
result = 0
for i in range(1,10000):
    result += i
print(result)
###
end_time = time.time() #종료 시간

print("알고리즘 수행 시간 : ", end_time - start_time)