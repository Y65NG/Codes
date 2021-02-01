def next_permutation(arr):
    index = len(arr) - 1
    while index > 0 and arr[index] < arr[index - 1] :
        index -= 1
    num = arr[index - 1]
    # print(num)
    for i in range(index, len(arr)):
        if arr[i] < num:
            # print('true')
            arr[index - 1], arr[i - 1] = arr[i - 1], arr[index - 1]
            break
        elif i == len(arr) - 1:
            arr[index - 1], arr[i] = arr[i], arr[index - 1]
            break
        
    rev = arr[index:]
    rev.reverse()
    arr = arr[:index] + rev
    return arr

while True: print(next_permutation(list(input())))
