

import math;

tc = int(input())


def handle_count(number):
    count = 0
    for i in range(number):
       if(math.gcd(i, number) == 1): count+=1
    return count   

def checkPrime(number):

    if number < 2: 
        return "NO"
    
    for i in range(2, number):

        if number % i == 0:
            return "NO"
        
    return "YES"


while tc  > 0:

    tc-= 1
    number = int(input())
    count = handle_count(number)
    print(checkPrime(count))
    
