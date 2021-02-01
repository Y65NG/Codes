T = int(input())
C = int(input())
chores = []
for i in range(C):
    chores.append(int(input()))
sum = 0
num = 0
while True:
    if sum + min(chores) > T: break
    else:
        sum += min(chores)
        index = chores.index(min(chores))
        del chores[index]
        num += 1
print(num)
