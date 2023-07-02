def reverse(x):
    if x < 0:
        is_negative = True
        x = abs(x)
    else:
        is_negative = False
    
    reversed_num = 0
    while x != 0:
        last_digit = x % 10
        reversed_num = (reversed_num * 10) + last_digit
        x = x // 10
    
    if is_negative:
        reversed_num *= -1
    
    if reversed_num < -231 or reversed_num > (231 - 1):
        return 0
    
    return reversed_num
