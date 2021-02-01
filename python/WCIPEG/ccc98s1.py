n = int(input())
for _ in range(n):
    line = input()
    words = line.split(' ')
    for word in range(len(words)):
        if len(words[word]) == 4: words[word] = '****'
    for i in words:
        print(i, end = ' ')
    print()