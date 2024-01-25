def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    lst = list()
    for num in range(a, b+1):
        sum = 0
        if num < 10:
            lst.append(num)
        else:
            l = len(str(num))
            n = num 
            while num // 1 != 0:
                sum += (num % 10)**l
                num //= 10
                l -= 1
            if n == sum:
                lst.append(n)
            
    return lst
