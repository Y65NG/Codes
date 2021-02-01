N = int(input())
for a in range(N):
    line = input()
    a = line.split(' ')[0]
    b = line.split(' ')[1]
    revA = a[::-1]
    revB = b[::-1]
    print(int(str(int(revA) + int(revB))[::-1]))
    