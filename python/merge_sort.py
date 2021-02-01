def merge_sort(arr, low, high):
    if low >= high: return
    mid = (low + high) // 2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)
    merge(arr, low, mid, high)
    return arr

def merge(arr, low, mid, high):
    if low >= high: return
    result = []
    left = low
    right = mid + 1
    index = low
    while True:
        if left > mid and right > high: break
        elif left > mid and right <= high:
            for i in range(right, high + 1):
                result.append(arr[i])
                index += 1
            # print(result)
            break
        elif left <= mid and right > high:
            for i in range(left, mid + 1):
                result.append(arr[i])
                index += 1
            # print(result)
            break
        elif arr[left] <= arr[right]:
            result.append(arr[left])
            left += 1
            index += 1
        elif arr[left] > arr[right]:
            result.append(arr[right])
            right += 1
            index += 1
    for i in range(low, index):
        arr[i] = result[i - low]
    # print(result)
    # return arr

arr = [3,-1,1,4,6,3,4,3,6,1,8]
print(merge_sort(arr, 0, len(arr) - 1))          
