def quick_sort(arr, low, high):
    if low >= high: return
    pivot = partition(arr, low, high)
    quick_sort(arr, low, pivot - 1)
    quick_sort(arr, pivot + 1, high)
    return arr
def partition(arr, low, high):
    pivot = low
    left = pivot + 1
    right = high
    l = False
    r = False
    while left != right + 1:
        if arr[left] <= arr[pivot] and left != right + 1: left += 1
        else: l = True
        if arr[right] >= arr[pivot] and left != right + 1: right -= 1
        else: r = True
        if l and r and left != right + 1:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            l = False
            r = False
    temp = arr[pivot]
    arr[pivot] = arr[right]
    arr[right] = temp
    return right

arr = [4,2,56,3,6,3,2]
print(quick_sort(arr, 0, len(arr) - 1))

