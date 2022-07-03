def solution(array, commands):
    
    temp = []
    answer = []
    for var in commands:
        i,j,k = list(map(int, var))
        temp = array[i-1:j]
        sort(temp)
        answer.append(temp[k-1])
    
    return answer

def sort(lists):
    for i in range(1, len(lists)):
        for j in range(i, 0, -1):
            if lists[j - 1] > lists[j]:
                lists[j - 1], lists[j] = lists[j], lists[j - 1]

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))