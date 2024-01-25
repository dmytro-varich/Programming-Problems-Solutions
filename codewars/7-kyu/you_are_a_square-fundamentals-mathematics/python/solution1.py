import math

def is_square(n):
    if n < 0:
        return False
    if n == 0:
        return True
    sqrt_n = math.isqrt(n)
    return sqrt_n * sqrt_n == n
