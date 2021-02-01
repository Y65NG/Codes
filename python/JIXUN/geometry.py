# point
def distance(u, v):
    return ((u[0] - v[0]) ** 2 + (u[1] - v[1]) ** 2) ** 0.5

# line
class Line:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
    
    def parallel(self, l):
        if self.a == l.a == 0 or self.b == l.b == 0: return True
        return self.a/self.b == l.a/l.b
    
    def intersect(self, l):
        a1, b1, c1 = self.a, self.b, self.c
        a2, b2, c2 = l.a, l.b, l.c
        return ((c2 * a1 - c1 * a2)/(b1 * a2 - b2 * a1),(c2 * b1 - c1 * b2)/(a2 * b1 - a1 * b2))

# vector
def dot_product(u, v):
    return u[0] * v[0] + u[1] * v[1]

def dot_line(u, l):
    