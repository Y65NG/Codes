import random
import time

while True:
	events = input('input your choices, split by space\n').split(' ')

	index = random.random() * len(events)
	#print(index)
	print('\nYour choice:', events[int(index)])
	print()
	time.sleep(0.5)
