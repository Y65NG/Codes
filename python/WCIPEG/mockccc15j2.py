P = int(input())
Q = int(input())
W = int(input())
import decimal
decimal.getcontext().rounding = 'ROUND_HALF_UP'
now_score = decimal.Decimal(P * (1 - W * 0.01) + 0.001).quantize(decimal.Decimal('0'))
# print(type(now_score))
diff = Q - int(now_score)


if diff <= W: print(int(diff / (W * 0.01)))
else: print('DROP THE COURSE')