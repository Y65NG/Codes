g = int(input())
for a in range(g):
    n = int(input())
    line = input()
    attr = line.split(' ')
    min = int(attr[0])
    max = int(attr[0])
    for i in attr:
        if int(i) < min: min = int(i)
        if int(i) > max: max = int(i)
    print(min, max)
    