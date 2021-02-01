def combine(arr, start):
    return arr[start + 1] + ' ' + arr[start + 2] + ' ' + arr[start]

def is_symbol(str):
    if str == '+' or str == '-': return True
    return False
    
while True:
    line = input()
    if line == '0': break
    formula = line.split(' ')
    index = 0
    while index < len(formula) - 2:
        
        if is_symbol(formula[index]) and not is_symbol(formula[index + 1]) and not is_symbol(formula[index + 2]):
            formula[index] = combine(formula, index)
            del formula[index + 1]
            del formula[index + 1]
            index = 0
        else: index += 1
    print(formula[0])
    