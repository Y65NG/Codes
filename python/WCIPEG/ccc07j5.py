motels = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]

def ways(start):
    if start == len(motels) - 1: return 1
    avaMotels = findNext(start)
    total = 0
    for next in avaMotels:
        total += ways(next)
    return total

def findNext(start):
    result = []
    for i in range(start + 1, len(motels)):
        diff = motels[i] - motels[start]
        if diff >= min and diff <= max:
            result.append(i)
    return result

min = int(input())
max = int(input())
n = int(input())
for i in range(n): 
    newMotel = int(input())
    for j in range(len(motels)):
        if newMotel < motels[j]:
            motels.insert(j, newMotel)
            break
print(ways(0))