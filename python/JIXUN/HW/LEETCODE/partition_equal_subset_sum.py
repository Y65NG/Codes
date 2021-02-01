def backpack(n, c, nums):
    memo = [[0] * (c + 1) for _ in range(n + 1)]
    memo[0] = [0] + [-float('inf') for _ in range(c)]
    for i in range(1, n + 1):
        for j in range(0, c + 1):
            up = memo[i - 1][j]
            if j - nums[i - 1] >= 0: left = memo[i - 1][j - nums[i - 1]]
            else: left = -float('inf')
            memo[i][j] = max(left, up)
    return memo[n][c]

def canPartition(nums):
    nums.sort()
    if sum(nums) % 2 != 0: return False
    c = sum(nums) // 2
    return backpack(len(nums), c, nums) != -float('inf')
print(canPartition([1,2,5]))
