# 冒泡排序: 比较相邻的元素，如果不符合，交换两个元素
def bubble_sort(arr):
    for last in range(len(arr) - 1, 0, -1):
        for cur in range(1, last + 1):
            if arr[cur] < arr[cur - 1]:
                arr[cur], arr[cur - 1] = arr[cur - 1], arr[cur]

# 插入排序: 将右边未排序的元素插入到左边排好序的元素
def insertion_sort(arr):
    for i in range(1, len(arr)):
        for sorted in range(0, i):
            if arr[sorted] >= arr[i]:
                arr.insert(sorted, arr[i])
                del arr[i + 1]

# 选择排序: 选目前最大元素跟最后元素交换


# 快速排序
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]: return False
    return True 

def quick_sort(arr, start, end):
    if start >= end: return
    if is_sorted(arr): return
    pivot = partition(arr, start, end)
    quick_sort(arr, start, pivot - 1)
    quick_sort(arr, pivot + 1, end)

def partition(arr, start, end):
    pivot = start
    left = pivot + 1
    right = end
    if left == right:
        arr[pivot], arr[left] = arr[left], arr[pivot]
        return pivot
    lstop = False
    rstop = False
    while left < right:
        if arr[left] < arr[pivot]: left += 1
        else: lstop = True
        if arr[right] >= arr[pivot]: right -= 1
        else: rstop = True
        if lstop and rstop: 
            arr[left], arr[right] = arr[right], arr[left]
            lstop = False
            rstop = False 
    if left == end: 
        arr[pivot], arr[end] = arr[end], arr[pivot]
        return end
    if right == start + 1:
        return pivot
    arr[pivot], arr[left - 1] = arr[left - 1], arr[pivot]
    return left - 1
arr = [3,54437,854,2346]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
