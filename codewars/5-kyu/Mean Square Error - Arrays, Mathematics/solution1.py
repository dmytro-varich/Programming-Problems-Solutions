def solution(array_a, array_b):
    res = [abs(array_b[i] - array_a[i])**2 for i in range(len(array_a))]
    return sum(res)/len(res)
