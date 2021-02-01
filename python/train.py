length = 0
result = ''
train = ''
a = ''
station = ''
b = ''

def initialize():
    
    
    result = ''
    a = ''
    b = ''
    station = ''
    train = ''
    
       
def isSorted(train):
    global station
    global a
    global b
    global length
    global result
    for i in range(1, length + 1):
        train += str(i)
        a += str(i)
    
    while(True):
        if (len(station) != 0) and (station[-1] == result[len[b]]):
            print(station[-1] + ' from station to b')
            b += station[-1]
            station = station[0: len(station) - 1]
        elif len(a) != 0 and a[0] == result[len(b)]:
            print(a[0] + ' from a to b')
            b += a[0]
            a = a[1:]
        elif len(a) != 0:
            print(a[0] + ' from a to station')
            station += a[0]
            a = a[1:]
        else:
            print('end')
            print('train:' + train)
            print('result' + result)
            if b == result: return True
            return False
            

while True:
    length = int(input())
    if(length == 0): break
    while True:
        line = input()
        if line == '0': 
            print()
            break
        initialize()
        for i in range(len(line)):
            if line[i] != ' ': result += line[i]
        if isSorted(train): print('Yes')
        else: print('No')
    
    
