def convert_number(input_number, from_base, to_base):
    # Validate input number
    if not input_number:
        return None, None, "No number provided.", None
    
    if input_number.startswith('0') and len(input_number) > 1:
        return None, None, "Invalid input: Numbers should not begin with Zero.", None
    
    if not input_number.isdigit():
        return None, None, "Invalid input: Please enter digits only.", None

    try:
        decimal_number = int(input_number, from_base)
    except ValueError:
        return None, None, "Invalid number for the selected base.", None
    
    if to_base not in [2, 8, 10, 16]:
        return None, None, "Invalid target base.", None
    
    if to_base == 2:
        return bin(decimal_number)[2:], "Binary", None, None
    elif to_base == 8:
        return oct(decimal_number)[2:], "Octal", None, None
    elif to_base == 16:
        return hex(decimal_number)[2:], "Hexadecimal", None, None
    else:
        return str(decimal_number), "Decimal", None, None
