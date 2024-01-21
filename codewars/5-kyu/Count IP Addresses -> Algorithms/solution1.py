def ips_between(start, end):
    start = [sum(int (x) * 256**idx for idx, x in enumerate(reversed(start.split("."))))]
    end = [sum(int (x) * 256**idx for idx, x in enumerate(reversed(end.split("."))))]
       
    return end[0] - start[0]
