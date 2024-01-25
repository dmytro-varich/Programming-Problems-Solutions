def move_zeros(lst):
    lst_zeros = [num for num in lst if num == 0]
    
    while 0 in lst:
        lst.remove(0)
    
    for zero in lst_zeros:
        lst.append(zero)
        
    return lst
