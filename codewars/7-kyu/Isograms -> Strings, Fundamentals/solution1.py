def string_to_lower(text):
    return text.lower()

def is_isogram(string):
    if string == "":
        return True
    for letter in string_to_lower(string):
        if string_to_lower(string).count(letter) > 1:
            print(string)
            return False
    return True
