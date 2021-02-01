line = input()
day_begin = int(line.split(' ')[0])
num_day = int(line.split(' ')[1])
print('Sun Mon Tue Wed Thr Fri Sat')
for i in range(day_begin - 1): print('   ', end = ' ')
for i in range(1, num_day + 1):
    if len(str(i)) == 1: print('  ' + str(i), end = ' ')
    else: print(' ' + str(i), end = ' ')
    if (i + day_begin - 1) % 7 == 0: print()