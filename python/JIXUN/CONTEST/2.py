import sys
import time
from collections import deque

lines = sys.stdin.read().strip().split('\n')
primes = {2,3,5,7,11,13,17,19,23,29,31,37}

def prime_sum(n1, n2):
    global primes
    return (n1 + n2) in primes

def valid(state):
    global n
    if len(state) == n and not prime_sum(state[0], state[-1]): return False
    if len(state) > 1 and not prime_sum(state[-1], state[-2]): return False
    return True

def goal(state):
    global n
    return len(state) == n and valid(state)

def neighbors(state):
    global n
    result = []
    last = (state[-1] % 2 == 0)
    for i in range1):
       if i not in state and (i % 2 == 0) != last and prime_sum(i, state[-1]): 
           new_state = state + [i] 
           result.append(new_state)
    # print(result)
    return result
    
def print_arr(arr):
    word = ''
    for i in range(len(arr)):
        if i == len(arr) - 1: 
            word += str(arr[i]) + '\n'
            # print(arr[i])
        else: 
            word += str(arr[i]) + ' '
            # print(arr[i], end = ' ') 
    return word

def backtrack(state):
    global result
    if not valid(state): return
    if goal(state): 
        result.append(state)
        return
    for next in neighbors(state):
        backtrack(next)

for _ in range(len(lines)):
    word = ''
    start = time.time()
    n = int(lines[_])
    result = []
    print('Case {}:'.format(_ + 1))
    backtrack([1])
    # print(result)
    for i in result: 
        # print(word)
        word += print_arr(i)
        # print(word)
    # if _ != len(lines) - 1: print()
    print(word)
    # print(time.time()- start)



