def find_outlier(integers):
    count = sum(1 for num in integers if num % 2 == 0) 
    
    if len(integers) - count == 1:
        result = [integer for integer in integers if integer % 2 != 0]
    else:
        result = [integer for integer in integers if integer % 2 == 0]
    
    return result[0]
