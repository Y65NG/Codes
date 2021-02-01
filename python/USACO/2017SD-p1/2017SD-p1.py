lines = open('homework.in').read().strip().split('\n')
n = int(lines[0])
questions = list(map(int, lines[1].split(' ')))
suffix = [0] * len(questions)
suffix[-1] = questions[-1]

for i in range(len(suffix) - 2, -1, -1):
	suffix[i] = suffix[i + 1] + questions[i]

#print(questions, suffix)
max_average = 0
k = []
min_score = min(questions)
min_index = questions.index(min_score)
for i in range(1, len(suffix) - 1):
	#print(k)
	score = suffix[i] - min_score
	if i == min_index:
		min_score = min(questions[i + 1:])
		min_index = questions.index(min_score)
	num = len(suffix) - i - 1
	average = score / num
	#print(score, num, average)
	if average > max_average:
		max_average = average
		k.clear()
		
	if average == max_average:
		k.append(i)
if questions[-1] > max_average:
	max_average = questions[-1]
	k = len(questions) - 1

result = ''
for i in k:
	result += str(i) + '\n'
print(result)
file = open('homework.out', 'w')
file.write(result)
file.close()
