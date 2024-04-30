def create_phone_number(n: list) -> str:
    phone_number = str()
    phone_number += "("
    
    for index, number in enumerate(n):
        if index == 3:
            phone_number += ") " + str(number)
        elif index == 6:
            phone_number += "-" + str(number) 
        else: 
            phone_number += str(number)
            
    return phone_number
