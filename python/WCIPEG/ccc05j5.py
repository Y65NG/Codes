# 判断一个字符串是否为 A-word
def isAW(word):
    if word == 'A': return True
    elif len(word) > 2 and word[0] == 'B' and word[-1] == 'S' and isAW(word[1:-1]): return True
    elif len(word) > 2 and word.find('N') != -1 and isAW(word[:word.find('N')]) and isAW(word[word.find('N') + 1:]): return True
    return False
while True:
    line = input()
    if line == 'X': break
    length = 3
    while length < len(line):
        start = 0
        while start < len(line) - length + 1:
            if isAW(line[start:start + length]):
                line = line[:start] + 'A' + line[start + length:]
                start = 0
            start += 1
        length += 1            
    if isAW(line): print('YES')
    else: print('NO')