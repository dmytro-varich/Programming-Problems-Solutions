convert_dict = {
    'M':  1000, 
    'CM': 900, 
    'D':  500, 
    'CD': 400, 
    'C':  100, 
    'XC': 90, 
    'L':  50, 
    'XL': 40, 
    'X':  10, 
    'IX': 9, 
    'V':  5, 
    'IV': 4, 
    'I':  1  
}

class RomanNumerals:
    @staticmethod
    def to_roman(target : int) -> str:
        result = ''
        for key, value in convert_dict.items():
            if value > target: continue 
            
            while target >= value and target != 0:            
                if target - value >= 0:
                    result += key
                    target -= value 
                  
            if target == 0: break
              
        return result

    @staticmethod
    def from_roman(roman_num : str) -> int:
        result = 0
        new_convert_dict = dict(sorted(convert_dict.items(), key=lambda item: len(item[0]), reverse=True))
        for key, value in new_convert_dict.items():
            if len(roman_num) == 0: break
            
            if key in roman_num:
                count = roman_num.count(key)
                result += value * count
                roman_num = roman_num.replace(key, '', count)
                
        return result
