def rearrangedString(s):
    alnum_s = ''
    for i in s:
        if i.isalnum():
            alnum_s += i
    alnum_s = str(sorted(alnum_s))
    print(alnum_s)