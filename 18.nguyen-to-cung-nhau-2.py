import math

tc  = int(input())


def reverse_string(s):
     return s[::-1]

def checkIsPrime(string):
    reverseString = reverse_string(string)
    if(math.gcd(int(string), int(reverseString)) == 1): return "YES"
    else: return "NO"
    return 
    

while tc > 0:
    tc -= 1
    string = input()
    print(checkIsPrime(string))
