lines = open('measurement.in').read().strip().split('\n')
N, G = [int(x) for x in lines[0].split(' ')]
calendar = []
cows = {}

for i in range(1, N + 1):
    date, cow, change = [int(x) for x in lines[i].split(' ')]
    calendar.append((date, cow, change))
    if cow not in cows: cows[cow] = G

calendar.sort()
count = 0
max_cows, max_yield = set(), G
for i in range(len(calendar)):
    cow, change = calendar[i][1:]
    cows[cow] += change
    
    if cow not in max_cows:
        cur_max = max_yield
        cur_max_cows = max_cows.copy()
        if cows[cow] > cur_max: 
            cur_max_cows = {cow}
            cur_max = cows[cow]
        elif cows[cow] == cur_max: 
            cur_max_cows.add(cow)
        
    else:
        if change < 0:
            cur_max_cows, cur_max = set(), max(cows.values())
            for j in cows:
                if cows[j] == cur_max:
                    cur_max_cows.add(j)
        else:
            cur_max_cows = {cow}
            cur_max = cows[cow]
    if cur_max_cows != max_cows:
        count += 1
        max_cows = cur_max_cows.copy()
    max_yield = cur_max
print(count)
file = open('measurement.out', 'w')
file.write(str(count))
file.close()