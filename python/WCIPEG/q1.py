T = int(input())
scores = []
for _ in range(T):
    scores.append(int(input()))
scores.sort()
# print(scores)
if len(scores) % 2 == 0:
    print('The median on the test is', (scores[len(scores) // 2 - 1] + scores[len(scores) // 2]) / 2)
else:
    print('The median on the test is', '%.1f' % scores[len(scores) // 2])