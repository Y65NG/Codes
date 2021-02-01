t = int(input())
for a in range(t):
    line = input()
    world = int(line.split('-')[0])
    level = int(line.split('-')[1])
    num = 1
    while True:
        if world == 8 and level == 4: 
            print(num)
            break
        elif world == 1 and level == 2: 
            world = 4
            level = 1
            # print('jump')
        elif world == 4 and level == 2:
            world = 8
            level = 1
            # print('jump')
        else:
            if level != 4:
                level += 1
                # print('level up')
            else: 
                world += 1
                level = 1
                # print('world up')
        num += 1
