import time
v = int(input('v\n'))
coins = list(map(int, input().split(' ')))
n = len(coins)
start = time.time()
def top_down(v, n, coins):
    memo = {}
    if v < 0: return 0
    # if n == 1: 
    #     if v % n == 0: return 1
    #     return 0
    if v == 0: return 1
    if n == 0: return 0
    # print(top_down(v - coins[n - 1], n, coins), top_down(v, n - 1, coins))
    if (v, n) in memo: return memo[(v, n)]
    result = top_down(v - coins[n - 1], n, coins) + top_down(v, n - 1, coins)
    memo[(v, n)] = result
    # print(memo)
    return result

def bottom_up(v, n, coins):
    memo = [[0 for i in range(n + 1)] for _ in range(v + 1)]
    memo[0] = [1] * (n + 1)
    for i in range(1, v + 1):
        for j in range(1, n + 1):
            # print(memo)
            if memo[i - coins[j - 1]][j] >= 0: up = memo[i - coins[j - 1]][j]
            left = memo[i][j - 1]
            memo[i][j] = up + left
            # print(memo)
    return memo[v][n]

def bottom_up2(v, n, coins):
    compressed_memo = [0] * (v + 1)
    compressed_memo[0] = 1
    
    for i in range(n):
        coin = coins[i]
        for j in range(coin, len(compressed_memo)):
            compressed_memo[j] = compressed_memo[j] + compressed_memo[j - coin]
            # print(compressed_memo)
    return compressed_memo[-1]

print(top_down(v, n, coins))
print(bottom_up(v, n, coins))
print(bottom_up2(v, n, coins))
# print()

# print(time.time() - start)