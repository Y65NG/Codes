T = int(input())
for a in range(T):
    N = int(input())
    max = 1
    for b in range(N):
        F = int(input())
        if F > max:
            max = F
    print(max)