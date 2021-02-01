k = int(input())
nums = []
for i in range(k):
    num = int(input())
    if num == 0: del nums[-1]
    else: nums.append(num)
# print(nums)
sum = 0
for i in nums: sum += i
print(sum)