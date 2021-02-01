N = int(input())
k = int(input())
sum = N
def shift(num): return num * 10
for i in range(k):
    N = shift(N)
    sum += N
print(sum)