import sys
lines = sys.stdin.read().strip().split('\n')
index = 0
# print(lines)
def check(capacity, vessels, numc):
    total = 0
    count = 1
    for i in vessels:
        if i > capacity: return False
        if total + i > capacity:
            total = i
            count += 1
        else: total += i
    return count <= numc
        
for _ in range(len(lines) // 2):
    # print(lines[0].split(' '))
    numc = int(lines[index].split(' ')[1])
    index += 1
    vessels = list(map(int, lines[index].split(' ')))
    index += 1
    high = sum(vessels)
    low = max(vessels) - 1
    while high - low > 1:
        # print(high, low)
        mid = (high + low) // 2
        if check(mid, vessels, numc): 
            high = mid
            # print('true')
        else: 
            low = mid
        # print(high, low)
    print(high)

