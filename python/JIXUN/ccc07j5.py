motels = {0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000}
memo = {}
A = int(input())
B = int(input())
m = int(input())
for _ in range(m):
    motels.add(int(input()))
def find_next(n):
    result = []
    for motel in motels:
        if (n + A) <= motel <= (n + B):
            result.append(motel)
    return result

def ways(n):
    if n == 7000: return 1
    total = 0
    # print(n, find_next(n))
    for next in find_next(n):
        if next in memo: total +=  memo[next]
        else: 
            total += ways(next)
            memo[next] = total
    return total
print(ways(0))