words = input().split(' ')
result = ''
if words[-1] == '': del words[-1]
def is_same_vowels_around(str, index):
    if (str[index + 1] == 'a' and str[index - 1] == 'a') or (str[index + 1] == 'e' and str[index - 1] == 'e') or (str[index + 1] == 'i' and str[index - 1] == 'i') or (str[index + 1] == 'o' and str[index - 1] == 'o') or (str[index + 1] == 'u' and str[index - 1] == 'u'):
        return True
    return False

def decode(str, start):
    index = str.find('p', start)
    if index == 0: index = str.find('p', start + 1)
    if index == -1: return str
    else:
        if is_same_vowels_around(str, index): 
            
            return str[:index] + str[index + 2:]

        else: return str[:index] + decode(str[index:], 0)
for i in range(len(words)):
    while decode(words[i], 0) != words[i]:
        words[i] = decode(words[i], 0)
        # print(words[i])
    result += words[i] + ' '
print(result[:-1])