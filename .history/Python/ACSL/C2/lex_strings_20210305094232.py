def rearrangedString(s):
    alnum_s = ''
    for i in s:
        if alnum(i):
            alnum_s += i
    alnum_s.sort()
    print(alnum_s)