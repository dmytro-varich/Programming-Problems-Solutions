def printer_error(s):
    count = 0
    alphabet = ['a', 'b', 'c', 
                'd', 'e', 'f',
                'g', 'h', 'i', 
                'j', 'k', 'l', 
                'm'
               ]
    
    for letter in s: 
        if letter not in alphabet:
            count += 1

    return f'{count}/{len(s)}'
