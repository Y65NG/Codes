t1 = int(input())
t2 = int(input())
length = 2
while t1 >= t2:
    t1, t2 = t2, t1 - t2
    length += 1
print(length)