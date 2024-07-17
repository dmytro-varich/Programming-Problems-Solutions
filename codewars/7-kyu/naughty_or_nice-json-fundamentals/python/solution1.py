from collections import Counter

def naughty_or_nice(data: dict) -> str:
    dct = {}
    
    for month in data.values():
        value_counts = Counter(month.values())
        for key, val in value_counts.items():
            if key not in dct:
                dct[key] = 0
            dct[key] += val 
            
    max_val = max(dct.values())
    result = sorted([key for key, value in dct.items() if value == max_val], key=len)
    return result[0] + "!"
