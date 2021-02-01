lines = open('shuffle.in').read().strip().split('\n')
N = int(lines[0])
rule = [int(x) - 1 for x in lines[1].split(' ')]
print(rule)
cows = list(range(N))
# print()
# print(cows)
def root(u):
    global cows
    while cows[u] != u: u = cows[u]
    return u

def union(u, v):
    global cows
    # if root(u) != root(v):
    #     cows[root(v)] = root(u)
    cows[u] = v

def find(u, v):
    return root(u) == root(v)

for i in range(len(rule)):
    union(i, rule[i])
    # print(cows)

print(cows)

# roots = set()
count = 0
for i in range(len(cows)):
    if cows[i] == i or i == cows[cows[i]] and cows[i] == cows[cows[cows[i]]]:
        count += 1
    # roots.add(root(cows[i]))
print(count)

file = open('shuffle.out', 'w')
file.write(str(count))
file.close()