T = int(input())
for _ in range(T):
    N = int(input())
    mountain = []
    branch = []
    lake = 1
    for __ in range(N):
        mountain.append(int(input()))
    while True:
        if len(mountain) > 0 and mountain[-1] == lake:
            # print(mountain[-1], 'from mountain to lake')
            del mountain[-1]
            lake += 1
        elif len(branch) > 0 and branch[-1] == lake:
            # print(branch[-1], 'from branch to lake')
            del branch[-1]
            lake += 1
        elif len(mountain) > 0:
            # print(mountain[-1], 'from mountain to branch')
            branch.append(mountain[-1])
            del mountain[-1]
        else: break
    # print(lake)
    if lake == N + 1: print('Y')
    else: print('N')