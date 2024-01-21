def get_middle(s):
    if len(s) % 2 == 0:
        while len(s) > 2:
            s = s[1:-1]
    else :
        while len(s) > 1:
            s = s[1:-1]
    return s
