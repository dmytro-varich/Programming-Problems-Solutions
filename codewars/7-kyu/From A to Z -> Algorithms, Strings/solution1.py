def gimme_the_letters(sp):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    
    if sp[0] == sp[2]: return sp[0]
    
    if sp[0].isupper(): alphabet = alphabet.upper()
    
    start = alphabet.index(sp[0])
    end = alphabet.index(sp[2])
    
    for a in range(start, end+1):
        result += alphabet[a]
        
    return result  
