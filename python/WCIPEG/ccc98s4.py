n = int(input())
for a in range(n):
    line = input()
    formula = []
    first = 0
    for i in range(len(line)):
        if line[i] == ' ':
            formula.append(line[first:i])
            first = i + 1
    formula.append(line[first:])
    index = 0
    while index < len(formula):
        if len(formula) > 3 and formula[index] == 'X':
            formula[index - 1] = '(' + formula[index - 1] + ' ' + formula[index] + ' ' + formula[index + 1] + ')'
            del formula[index]
            del formula[index]
            index = 0
        else: index += 1
    index = 0
    while index < len(formula):
        if len(formula) > 3 and (formula[index] == '+' or formula[index] == '-'):
            formula[index - 1] = '(' + formula[index - 1] + ' ' + formula[index] + ' ' + formula[index + 1] + ')'
            del formula[index]
            del formula[index]
            index = 0
        else: index += 1
    
    for i in formula: print(i, end = ' ')
    print()