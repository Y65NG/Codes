# Task: Your Ride Is Here
comet, group = open('ride.in').read().strip().split('\n')
n1, n2 = 0
for i in comet:
	n1 *= ord(i)

for i in group:
	n2 *= ord(i)

file = open('ride.out', 'w')
if n1 % 47 == n2 % 47: file.write('GO')
else: file.write('STAY')
file.close()
