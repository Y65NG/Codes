import math
import sys

def distance(u, v):
    return ((u[0] - v[0]) ** 2 + (u[1] - v[1]) ** 2) ** 0.5

# def angle(u, v):
#     return math.atan2(abs(v[1] - u[1]), abs(v[0] - u[0]))

def shortest_distance(points):
    shortest = float('inf')
    shortest_points = ()
    for u in range(len(points) - 1):
        for v in range(u + 1, len(points)):
            if distance(points[u], points[v]) < shortest: 
                shortest = distance(points[u], points[v])
                shortest_points = (points[u], points[v])
    return (shortest, shortest_points)

# def side(distance, angle):
#     x = distance * math.sin(angle)
#     y = distance * math.cos(angle)
#     return int(max(x, y))

def side(u, v):
    dx = abs(u[0] - v[0])
    dy = abs(u[1] - v[1])
    return max(dx, dy)

lines = sys.stdin.read().strip().split('\n')
_ = 0
while _ < len(lines):
    N = int(lines[_])
    _ += 1
    points = []
    for i in range(_, N + _):
        point = tuple(map(int, lines[i].split(' ')))
        points.append(point)
        _ += 1
    points.sort()
    p = shortest_distance(points)[1]
    print(side(p[0], p[1]))

