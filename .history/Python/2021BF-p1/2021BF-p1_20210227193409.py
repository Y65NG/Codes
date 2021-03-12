import sys
animals = ['Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig', 'Rat']
def changeToYear(pos, animal1, animal2):
    i1, i2 = animals.index(animal1), animals.index(animal2)
    if pos == 'previous':
        if i1 < i2: return -(i2 - i1)
        elif i1 > i2: return (i1 - i2) - 12
        else: return -12
    else: 
        if i1 < i2: return 12 - (i2 - i1)
        elif i1 > i2: return i1 - i2
        else: return 12

lines = sys.stdin.read().strip().split('\n')
N = int(lines[0])
names = {}
for i in range(1, N + 1):
    words = lines[i].split(' ')
    name, pos, animal, name2 = words[-1], words[3], words[4]

name = 'Elsie'
year = 0
while name != 'Bessie':
    year += names[name][0]
    
    name = names[name][1]
    print(year, name)
print(year)


