def find_missing_letter(chars):
    index = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"    # English alphabet

    if chars[0].isupper():
        alphabet = alphabet.upper()

    for idx, letter in enumerate(alphabet):
        if chars[0] == alphabet[idx]:
            index = idx
    
    for idx, char in enumerate(chars):        
            if alphabet[index] != chars[idx]:
                return alphabet[index]
            index += 1
