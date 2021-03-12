import sys
animals = ['Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig', 'Rat']
def changeToYear(pos, animal):
    if pos == 'previous':
        for i in range(len(animals)):
            if animal == animals[i]: 
                return -(12 - i)
    else: 
        for i in range(len(animals)):
            if animal == animals[i]: 
                if i == 0: return 12
                return i

lines = sys.stdin.read().strip().split('\n')
N = int(lines[0])
names = {}
for i in range(1, N + 1):
    words = lines[i].split(' ')
    name, pos, animal, name2 = words[0], words[3], words[4], words[-1]
    names[name] = (changeToYear(pos, animal), name2)

name = 'Elsie'
year = 0
while name != 'Bessie':
    year += names[name][0]
    name = names[name][1]
print(year)


