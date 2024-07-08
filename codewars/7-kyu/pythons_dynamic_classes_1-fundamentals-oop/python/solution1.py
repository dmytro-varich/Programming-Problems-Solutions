import re 

def class_name_changer(cls, new_name):
    pattern = r'^[A-Z][a-zA-Z0-9]*$'    
    if re.match(pattern, new_name):
        cls.__name__ = new_name
    else: 
        raise Exception 
