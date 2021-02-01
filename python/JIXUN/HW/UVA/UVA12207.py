from collections import deque
case = 1
while True:
    data = input()
    if data == '0 0': break
    print('Case {}:'.format(case))
    P = int(data.split(' ')[0])
    que = deque(list(range(1, P + 1)))
    C = int(data.split(' ')[1])
    count = 0
    for _ in range(C):
        command = input()
        if command == 'N': 
            admit = que.popleft()
            print(admit)
            que.append(admit)
        else:
            num = int(command.split(' ')[1])
            que.remove(num)
            que.appendleft(num)
