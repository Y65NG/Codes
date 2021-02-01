n = int(input())
end = n
paths = []
mem = []
while True:
    line = input()
    if line == '0 0': break
    paths.append(line.split(' '))
for i in range(10000): mem.append(-1)
    
# print(paths)
def ways(start):
    global paths
    global end
    global mem
    
    total = 0
    if start == end: return 1
    if mem[start] != -1: return mem[start]
    for i in paths:
        if int(i[0]) == start:
            # print('from', start, 'to', i[1])
            total += ways(int(i[1]))
            mem[start] = ways(int(i[1]))
            # print(total)
    return total
# print(mem)
print(ways(1))
    
