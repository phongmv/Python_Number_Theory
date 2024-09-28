import math

def rv_string(s):
    return s[::-1]

def is_dub_prime(s):
    if(math.gcd(int(s), int(rv_string(s))) == 1): return "YES"
    else: return "NO"

tc  = int(input())

while tc >0:
    tc -= 1
    s = input()
    print(is_dub_prime(s))
