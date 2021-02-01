import sys
lines = open('2.in', 'r').read().strip().split('\n')
# lines = sys.stdin.read().strip().split('\n')
N, M, C = list(map(int, lines[0].split(' ')))
if N == 1: 
    print('0')
    file = open('convention.out', 'w')
    file.write('0')
    file.close()
else:
    times = list(map(int, lines[1].split(' ')))
    times.sort()
    #print(times)
    def check(mid,times, N, M, C):
        index = 0
        cur = 0
        max_time = times[0] + mid
        
        while M > 0 and index < len(times):
            
            # print(cur)
            if cur < C and max_time >= times[index]:
                # print('t')
                #print(max_time)
                cur += 1
                index += 1
            else: 
                # print('f')
                max_time = times[index] + mid
                M -= 1
                cur = 0
                
        return index > len(times) - 1
            
    high = max(times) - min(times)
    low = -1

    while high - low > 1:
        # print(high, low)
        mid = (high + low) // 2
        if check(mid, times, N, M, C): high = mid
        else: low = mid
        # print(high, low)
    print(high)
    file = open('convention.out', 'w')
    file.write('{}\n'.format(str(high)))
    file.close()
