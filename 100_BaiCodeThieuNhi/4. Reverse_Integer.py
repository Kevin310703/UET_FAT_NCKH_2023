def reverse(x):
    if x < 0:
        is_negative = True
        x = abs(x)
    else:
        is_negative = False
    
    reversed_num = 0
    while x != 0:
        
        reversed_num = (reversed_num * 10) + x%10
        x = x // 10
    
    
    if is_negative:
        reversed_num *= -1
    
   
    
    return reversed_num
num = input("Nhap 1 so: ")
print(reverse(num))
