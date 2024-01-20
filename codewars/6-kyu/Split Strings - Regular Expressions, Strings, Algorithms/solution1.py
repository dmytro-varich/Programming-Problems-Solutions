def solution(s):
    if len(s) % 2 != 0:
        s += '_'
    
    return [s[idx-1] + s[idx] for idx, char in enumerate(s) if idx % 2 != 0]