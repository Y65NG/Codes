location = 1
while True:
    step = int(input())
    if step == 0: 
        print('You Quit!')
        break
    if not location + step > 100:
        location += step
    print('You are now on square', end = ' ')
    if location == 54: location = 19
    elif location == 90: location = 48
    elif location == 99: location = 77
    elif location == 9: location = 34
    elif location == 40: location = 64
    elif location == 67: location = 86
    print(location)
    if location == 100: 
        print('You Win!')
        break

