
        
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    less,equal,great = [],[],[]
    for num in arr:
        if num < pivot:
            less.append(num)
        elif num > pivot:
            great.append(num)
        else:
            equal.append(num)
    return quicksort(less) + equal + quicksort(great)

nums1 = [1,2,3,0,0,0]
nums2 = [2,3,4]
m = 3
n = 3
nums1 = nums1[:m]+nums2[:n]
print(nums1)
print(quicksort(nums1))
