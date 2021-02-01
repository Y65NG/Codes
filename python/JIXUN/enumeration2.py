line = input().split(' ')
A, B, C = int(line[0]), int(line[1]), int(line[2])
for x in range(-100, 101):
    for y in range(-100, 101):
        z = A - x - y
        if x != y and x != z and y != z and x + y + z == A and x * y * z == B and x ** 2 + y ** 2 + z ** 2:
            print(x,y,z)
