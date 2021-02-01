T = int(input())
for a in range(T):
    N = int(input())
    statuses = []
    for b in range(N):
        line = input().split(' ')
        A = int(line[0])
        S = int(line[1])
        O = int(line[2])
        turn = A + S
        status = []
        index = O
        for i in range(turn):
            if index >= turn: index -= turn
            if index < A: 
                status.append(1)
                index += 1
            elif index >= A: 
                status.append(0)
                index += 1
        statuses.append(status)
        
    # print(statuses)
    multiple = 1
    for i in range(N):
        multiple *= len(statuses[i])
    for i in range(N):
        statuses[i] *= multiple // len(statuses[i])
    for i in range(len(statuses[0])):
        if N == 1:
            if statuses[0][i] == 0:
                print(i)
                break
        elif N == 2:

            if statuses[0][i] == 0 and statuses[1][i] == 0:
                print(i)
                break
        elif N == 3:
            if statuses[0][i] == 0 and statuses[1][i] == 0 and statuses[2][i] == 0:
                print(i)
                break
        else:
            if statuses[0][i] == 0 and statuses[1][i] == 0 and statuses[2][i] == 0 and statuses[3][i] == 0:
                print(i)
                break
    else: print('Foxen are too powerful')
    

