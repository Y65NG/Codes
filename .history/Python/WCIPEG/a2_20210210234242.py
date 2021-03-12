print('Ready')
while True:
    line = input()
    if line == '  ': break
    if ('q' in line and 'p' in line) or ('d' in line and 'b' in line):
        print('Mirrored pair')
    else:
        print('Ordinary pair');
    