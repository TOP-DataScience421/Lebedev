decimal_to_base_mapping = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F',
    16: 'G',
    17: 'H',
    18: 'I',
    19: 'J',
    20: 'K',
    21: 'L',
    22: 'N',
    23: 'O',
    24: 'P',
    25: 'Q',
    26: 'R',
    27: 'S',
    28: 'T',
    29: 'U',
    30: 'V'
}

def int_base(number_to_convert: str, current_base: int, transform_base: int) -> str | None:
    if current_base not in range(2, 37) or transform_base not in range(2, 37):
        return None
    
    check = check_number_in_base(number_to_convert, current_base)
    if check == False:
        return None
        
    decimal_num = convert_to_decimal(number_to_convert, current_base)
    
    result = convert_to_transform_base(decimal_num, transform_base)
    
    return result

def check_number_in_base(number: str, base: int) -> bool:
    try:
        int(number, base)
        return True
    except ValueError:
        return False
        
def convert_to_decimal(number: str, base: int) -> str:
    decimal_num = str(int(number, base))
    return decimal_num

def convert_to_transform_base(number: str, base: int) -> str:
    num_list = []
    number = int(number)
    if base <= 11:
        while number > 0:
            remaind = number % base
            num_list.insert(0, remaind)
            number = number // base
        result = ''.join(map(str, num_list))
        return result
    else:
        while number > 0:
            remaind = number % base
            if remaind < 10:
                num_list.insert(0, remaind)
                number = number // base
            else:
                value = decimal_to_base_mapping.get(remaind)
                num_list.insert(0, value)
                number = number // base
        result = ''.join(map(str, num_list))
        return result
    
#>>> int_base('ff00', 16, 2)
#'1111111100000000'
#>>> int_base('1101010', 2, 30)
'3G'
#>>> int_base('V456GHJ', 32, 14)
#'18913B8C39'