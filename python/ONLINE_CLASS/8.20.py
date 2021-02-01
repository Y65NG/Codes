import heapq
from collections import deque
# Q0
def heap_sort(lst):
    heapq.heapify(lst)
    result = lst[:]
    lst.clear()
    while len(result) > 0:
        lst.append(heapq.heappop(result))

# Q1
def has_duplicate(lst):
    init = len(lst)
    lst = set(lst)
    if len(lst) < init: return True
    return False

# Q1
def has_sum(lst, N):
    lst = set(lst)
    for i in lst:
        if N - i in lst and N - i != i: return True
    return False

# Q2
def k_largest(lst, k):
    for i in range(len(lst)): lst[i] = -lst[i]
    heapq.heapify(lst)
    for i in range(k - 1): heapq.heappop(lst)
    return -heapq.heappop(lst) 

# 复杂度: O(NlogK)
def k_largest2(lst, k):
    largest = []
    for i in range(k): heapq.heappush(largest, lst[i])
    for j in range(k, len(lst)):
        current = lst[j]
        if current > largest[0]: # min heap 的根节点 (largest[0]) 就是 heap 中的最小值
            heapq.heappop(largest)
            heapq.heappush(largest, current)
        return largest[0]

# Q3
def num_balloons(text):
    nums = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}
    total = 0
    for chr in text: 
        if chr in nums: nums[chr] += 1
    while True:
        if nums['b'] > 0 and nums['a'] > 0 and nums['l'] > 1 and nums['o'] > 1 and nums['n'] > 0:
            total += 1
            nums['b'] -= 1
            nums['a'] -= 1
            nums['l'] -= 2
            nums['o'] -= 2
            nums['n'] -= 1
        else: break
    return total

def num_balloons2(text):
    counts = {}
    for ch in text:
        if ch in counts: counts[ch] += 1
        else: counts[ch] = 1
    return min(counts['b'], counts['a'], counts['l'] // 2, counts['o'] // 2, counts['n'], counts['s'])

# Q4
def ugly_number2(n):
    to_explore = [(1,0,0,0)] # (product, 2^0 * 3^0 * 5^0)
    count = 1
    visited = set()
    while count < n:
        product, x, y, z = heapq.heappop(to_explore)
        
        # 根据目前的 x, y, z 生成下一组可能的 x, y, z
        for t in [(product * 2, x + 1, y, z), (product * 3, x, y + 1, z), (product * 5, x, y, z + 1)]:
            if t not in visited:
                heapq.heappush(to_explore, t)
                visited.add(t)
        count += 1
    product, x, y, z = heapq.heappop(to_explore)
    return product
ugly_number2(5)