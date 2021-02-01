t = int(input())
for a in range(t):
    n = int(input())
    first = input()
    second = input()
    result = ''
    firstInd = len(first) - 1
    secondInd = len(second) - 1
    while firstInd >= 0 and secondInd >= 0:
        #if secondInd >= 0:
        result += second[secondInd]
        secondInd -= 1
        #if firstInd >= 0:
        result += first[firstInd]
        firstInd -= 1
        
    print(result)