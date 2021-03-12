def rearrangedString(s):
    alnum_s = ''
    for i in s:
        if i.isalnum():
            alnum_s += i
    alnum_s = ''.join(sorted(alnum_s))
    # print(alnum_s)
    
    letters = {}
    blocks = ['' for i in range(101)]
    for i in alnum_s:
        if i not in letters: letters[i] = 1
        else: letters[i] += 1
    for letter in letters:
        if blocks[letters[letter]] == '': blocks[letters[letter]] = [letter]
        else: blocks[letters[letter]].append(letter)
    
    temp = []
    count = 0
    for i in range(101):
        if blocks[i] != '':
            if count % 2 == 0: temp.append(str(i) + ''.join(sorted(blocks[i])) + ',')
            else: temp.append(str(i) + ''.join(sorted(blocks[i], reverse = True)) + ',')
            count += 1
    
    result = result[:-2]
    return result
