def god_control(num1, oper, num2):
    if oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    elif oper == '*':
        return num1 * num2
    elif oper == '/':
        return num1 // num2
#-----------------------------------------------------------
def zero(function = None): 
    if function is None:
        return 0
    return god_control(0, function[1], function[0])

def one(function = None): 
    if function is None:
        return 1
    return god_control(1, function[1], function[0])

def two(function = None): 
    if function is None:
        return 2
    return god_control(2, function[1], function[0])

def three(function = None): 
    if function is None:
        return 3
    return god_control(3, function[1], function[0])

def four(function = None):
    if function is None:
        return 4
    return god_control(4, function[1], function[0])

def five(function = None): 
    if function is None:
        return 5
    return god_control(5, function[1], function[0])

def six(function = None): 
    if function is None:
        return 6
    return god_control(6, function[1], function[0])

def seven(function = None): 
    if function is None:
        return 7
    return god_control(7, function[1], function[0])

def eight(function = None): 
    if function is None:
        return 8
    return god_control(8, function[1], function[0])

def nine(function = None): 
    if function is None:
        return 9
    return god_control(9, function[1], function[0])
#-----------------------------------------------------------  
def plus(number = None): 
    return number, "+"
def minus(number = None): 
    return number, "-"
def times(number = None): 
    return number, "*"
def divided_by(number = None): 
    return number, "/"
