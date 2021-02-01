n = int(input())
for a in range(1, n + 1):
    line = input()
    index = int(line.split(' ')[0])
    word = line.split(' ')[1]
    if index <= 0: pass
    # elif index == 1: word = word[index:]
    elif index < len(word): word = word[:index - 1] + word[index:]
    else: word = word[:index - 1]
    print(a, word)