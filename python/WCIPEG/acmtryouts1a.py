N = int(input())
for a in range(N):
    line = input()
    if line == 'Scissors':
        print('Rock')
    elif line == 'Rock':
        print('Paper')
    elif line == 'Paper':
        print('Scissors')
    elif line == 'Fox':
        print('Foxen')
    elif line == 'Foxen':
        break