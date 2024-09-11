import math

tc = int(input())

def hd_rounded(number, string):

    cnt = len(string) - 1
    l = 1

    while l <= cnt:

        dv_number = pow(10, l)
        
        rm_number = number % dv_number

        number -= rm_number

        if rm_number >= dv_number/2:
            number += dv_number

        l+=1

    return number

# Vòng lặp xử lý các test case
while tc > 0:
    tc -= 1
    str_num = input() 
    number = int(str_num) 
    print(hd_rounded(number, str_num)) 
