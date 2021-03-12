def rearrangedString(s):
    alnum_s = ''
    for i in s:
        if i.isalnum():
            alnum_s += i
    alnum_s = ''.join(sorted(alnum_s))
    print(alnum_s)
    
    letters = {}
    blocks = ['' for i in range(101)]
    for i in alnum_s:
        if i not in letters: letters[i] = 1
        else: letters[i] += 1
    print(letters)
