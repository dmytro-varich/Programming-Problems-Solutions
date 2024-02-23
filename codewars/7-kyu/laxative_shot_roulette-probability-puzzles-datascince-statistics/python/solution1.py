from math import comb

def get_chance(n: int, x: int, a: int) -> float:
    numerator = comb(n-x, a)
    denominator = comb(n, a)
    probality = numerator / denominator
    result = round(float(f"{probality:.2g}"), 2)
    return result
