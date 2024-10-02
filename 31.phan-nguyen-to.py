import math

def gcd_counter(number):
    cnt = 0
    for i in range(1, int(math.sqrt(number) + 1)):
        if(number % i == 0): cnt += 1
    return cnt


def checked_counter(number): 
   
    checked_number = number
    x_cnt  = gcd_counter(number)
   
    while True:
        checked_number += 1
        ck_cnt = gcd_counter(checked_number)
        if(ck_cnt > x_cnt):
            return checked_number


tc = int(input())
while tc > 0:
    tc -= 1
    number = int(input())
    print(checked_counter(number))


