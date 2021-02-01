def valid(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            xa, ya = i, arr[i]
            xb, yb = j, arr[j]
            if xa == xb: return False
            if ya == yb: return False
            if abs(xa - xb) == abs(ya - yb): return False
    return True
count = 0 
for q1 in range(8):
    for q2 in range(8):
        for q3 in range(8):
            for q4 in range(8):
                for q5 in range(8):
                    for q6 in range(8):
                        for q7 in range(8):
                            for q8 in range(8):
                                if valid([q1,q2,q3,q4,q5,q6,q7,q8]):
                                    print(q1,q2,q3,q4,q5,q6,q7,q8)
                                    count += 1
print(count)

            