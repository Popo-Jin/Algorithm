num = [-4,9,12,-42,0,3,4,6,7]

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    less_arr, equal_arr, great_arr = [], [], []
    for num in arr:
        if num < 0:
            num *= -1
        if num < pivot:
            less_arr.append(num)
        elif num == pivot:
            equal_arr.append(num)
        else:
            great_arr.append(num)  
    return quicksort(less_arr) + equal_arr + quicksort(great_arr)

result = quicksort(num)
result_arr = []
for a in result:
    a *= a
    result_arr.append(a)
print(result_arr)

