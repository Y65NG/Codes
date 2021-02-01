solutions = []
def fibo(n):
    global solutions
    if n == 0 or n == 1: return 1
    if solutions[n] != -1: return solutions[n]
    result = fibo(n - 1) + fibo(n - 2)
    solutions[n] = result
    return result

while True:
    n = int(input())
    for i in range(n + 1):
        solutions.append(-1)
    print(fibo(n))
