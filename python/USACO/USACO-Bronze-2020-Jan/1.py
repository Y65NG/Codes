line = list(map(int, input().split(' ')))
abc = max(line)
line.remove(abc)
a = min(line)
line.remove(a)
b = min(line)
line.remove(b)
c = abc - a - b
print(a, b, c)
