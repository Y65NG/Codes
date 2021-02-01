word = input()
letters = []
for letter in word: letters.append(letter)

def is_vowel(letter):
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        return True
    return False

def replace(letter):
    result = letter
    if is_vowel(letter): return letter
    else:
        # 左右两个指针
        left = ord(letter)
        right = ord(letter)
        # 寻找第二个字母
        while True:
            if left > 97: left -= 1
            if right < 122: right += 1
            # print(left, right)
            if is_vowel(chr(left)) and is_vowel(chr(right)): 
                result += chr(left)
                break
            elif is_vowel(chr(left)): 
                result += chr(left)
                break
            elif is_vowel(chr(right)): 
                result += chr(right)
                break
        
        # 寻找第三个字母
        index = ord(letter) 
        while True:
            if index < 122: index += 1
            # print(chr(index))

            if not is_vowel(chr(index)):
                result += chr(index)
                break
        return result

for i in range(len(letters)):
    letters[i] = replace(letters[i])
    print(letters[i], end = '')
