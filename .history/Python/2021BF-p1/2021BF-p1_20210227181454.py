import sys
animals = ['Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig', 'Rat']
def changeToYear(pos, animal):
    if pos == 'previous':
        for i in range(len(animals)):
            if animal == animals[i]: return 12 - i

lines = sys.stdin.read().strip().split('\n')
N = int(lines[0])
names = {}
for i in range(1, N + 1):
    words = lines[i].split(' ')
    name,  = words[0]

