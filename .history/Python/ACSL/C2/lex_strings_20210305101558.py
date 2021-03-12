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
    
    result = ''
    count = 0
    for i in range(100, -1, -1):
        if blocks[i] != '':
            if count % 2 == 0: result.append(str(i) + ''.join(sorted(blocks[i])) + ',')
            else: result.append(str(i) + ''.join(sorted(blocks[i], reverse = True)) + ',')
            count += 1
    
    print(result[:-1])
    
    return result[:-1]
