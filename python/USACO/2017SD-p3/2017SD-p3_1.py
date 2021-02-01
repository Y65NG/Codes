lines = open('shuffle.in').read().strip().split('\n')
N = int(lines[0])
rule = [int(x) - 1 for x in lines[1].split(' ')]
# print(rule)
cows = list(range(N))
# print()
# print(cows)
roots = set()
cache = list(range(N))
def find(i):
    global rule, roots, cache
    visited = set()
    # if cache[i] != i:
    temp = i
    if cache[temp] == temp:
        while rule[temp] not in visited:
            temp = rule[temp]
            visited.add(temp)
        roots.add(temp)
        roots.add(rule[temp])
        cache[i] = temp

for i in range(len(rule)):
    # print(i)
    find(i)
    # print(cows)

# print(roots)
print(len(roots))


file = open('shuffle.out', 'w')
file.write(str(len(roots)))
file.close()