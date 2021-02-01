# Q-1
list1 = [False] * 993
list2 = [False for x in range(993)]

# Q0 & Q1
def sum_of_list(arr):
    total = 0
    for i in arr: total += i
    return total

# Q2
word = 'apple'
result = ''
for i in range(len(word) - 1, -1, -1):
    result += word[i]
print(result)

# Q3
def has22(arr):
    for i in range(len(arr) - 1):
        if arr[i] == 2 and arr[i + 1] == 2: return True
    return False

# Q4
def is_increasing(arr):
    for i in range(len(arr) - 1):
        if arr[i + 1] <= arr[i]: return False
    return True

# Q5
def xyz_there(str):
    start = 0
    while True:
        index = str.find('xyz', start)
        if index == 0 or index > 0 and str[index - 1] != '.': return True
        else: start = index + 1
        if start == 0: break
    return False

# Q6
def encrypt(str):
    result = ''
    for letter in str:
        result += chr(((ord(letter) - ord('a') + 5) % 26) + ord('a'))
    return result

def decrypt(str):
    result = ''
    for letter in str:
        result += chr(((ord(letter) - ord('a') - 5) % 26) + ord('a'))
    return result

#Q7
def running_sum(arr):
    result = []
    total = 0
    for num in arr:
        total += num
        result.append(total)
    return result
