while True:
    word = input()
    if word == 'quit!': break
    if len(word) > 4:
        if word[-3] != 'a' and word[-3] != 'e' and word[-3] != 'i' and word[-3] != 'o' and word[-3] != 'u' and word[-3] != 'y':
            if word[-2:] == 'or':
                word = word[:-1] + 'u' + word[-1]
    print(word)