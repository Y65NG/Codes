import itertools

t = int(input())

# def num_1(state):
#     result = 0
#     for i in state: 
#         if i == 1: result += 1
#     return result

# def check(state):
#     global n, k
#     return len(state) <= n and num_1(state) <= k

# def generate(state):
def combine(tup):
    result = ''
    for i in tup: result += str(i)
    return int(result)


def generate(n, k):
    bits = [1] * k + [0] * (n - k)
    return set(itertools.permutations(bits))

def fill(num):
    global n, k
    num = str(num)
    supply = ''
    for i in range(n - len(num)): supply += '0'
    return supply + num

def print_set(bits):
    bits = list(map(combine, list(bits)))
    # print(bits)
    bits = sorted(bits, reverse = True)
    for bit in bits: print(fill(bit))

for _ in range(t):
    line = tuple(map(int, input().split(' ')))
    print('The bit patterns are')
    n, k = line[0], line[1]
    bits = generate(line[0], line[1])
    print_set(bits)

    