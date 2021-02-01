total_scores = [0]
for _ in range(1, 6):
    line = input()
    scores = line.split(' ')
    total = 0
    for i in scores: total += int(i)
    total_scores.append(total)
print(total_scores.index(max(total_scores)), max(total_scores))
    