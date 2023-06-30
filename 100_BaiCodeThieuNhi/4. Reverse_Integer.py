"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value 
to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

    Input: x = 123
    Output: 321

Example 2:

    Input: x = -123
    Output: -321

Example 3:

    Input: x = 120
    Output: 21

"""
def solatnguoc(n) :
    if n>-231 and n<230:
        lat = 0
        while n != 0 :
            lat = lat*10 + n%10
            n //= 10
        return lat 
    
    else:
        print("Nhap 1 so lon hon -231 va be hon 230")
x = int(input("nhap 1 so: "))

result = solatnguoc(x)
print (result)

