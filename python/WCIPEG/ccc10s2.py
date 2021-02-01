num = int(input())
letter = {}
for i in range(num):
    line = input()
    letter[line.split(' ')[0]] = line.split(' ')[1]
code = input()
while len(code) > 0:
    for key, value in letter.items():
        if code.find(value) == 0:
            print(key, end = '')
            code = code[len(letter[key]):]
            
