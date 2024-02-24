from preloaded import LOVE_LANGUAGES

def love_language(partner, weeks):
    stats = {
        "words":  0, 
        "acts" :  0, 
        "gifts":  0, 
        "time" :  0, 
        "touch":  0
    }
    n = 0
    i = 0
    while n < weeks*7: 
        if i > 4: i = 0
        if 'positive' == partner.response(LOVE_LANGUAGES[i]):
            stats[LOVE_LANGUAGES[i]] += 1
        else:
            stats[LOVE_LANGUAGES[i]] -= 1
            
        n += 1
        i += 1
        
    result = max(stats.keys(), key = lambda k: stats[k])
    
    return result
