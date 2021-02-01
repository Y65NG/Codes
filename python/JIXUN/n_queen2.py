
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

def valid(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            xa, ya = i, arr[i]
            xb, yb = j, arr[j]
            if xa == xb: return False
            if ya == yb: return False
            if abs(xa - xb) == abs(ya - yb): return False
    return True

def n_queens(queens, n):
    count = 0
    result = n
    while n > 1:
        result = n * (n - 1)
        n -= 1
    for i in range(result - 1):
        if valid(queens): 
            print(queens)
            count += 1
        queens = next_permutation(queens)
    print(count)
n_queens([0,1,2,3,4,5,6,7],8)