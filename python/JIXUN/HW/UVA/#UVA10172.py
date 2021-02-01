from collections import deque
SET = int(input())
for _ in range(SET):
    time = 0
    carrier = deque() # stack
    data = input().split(' ')
    N = int(data[0])
    S = int(data[1])
    Q = int(data[2])
    stations = []
    for i in range(N):
        line = input().split(' ')
        Qi = int(line[0])
        B = deque() # queue
        for des in range(1, Qi + 1): 
            B.append(int(line[des]))
        stations.append(B)
    station = 1
    while True:    
        # 卸货
        while True:
            if len(carrier) != 0 and carrier[-1] == station: 
                carrier.pop() 
                time += 1
            elif len(carrier) != 0: 
                stations[station - 1].append(carrier.pop())
                time += 1
            
            if len(carrier) == 0 or (len(stations[station - 1]) == Q and carrier[-1] != station): break
        # print(carrier,stations,time)
        # 装货
        for cargo in range(S - len(carrier)):
            if len(stations[station - 1]) != 0:
                carrier.append(stations[station - 1].popleft())
                time += 1
        if len(carrier) == 0:
            
            lenthB = 0
            for j in range(len(stations)):
                lenthB += len(stations[j])
            if lenthB == 0: break
        time += 2
        station += 1

        if station > 5: station = 1
        n = 1
        
    print(time)



        