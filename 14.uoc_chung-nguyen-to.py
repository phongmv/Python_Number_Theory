import math

tc = int(input())


def isPrime(n):

    s = str(n)
    sum = 0
    for c in s:
       sum += int(c);     

    if(sum < 2): return "NO"

    for i in range(2, sum):
        if(sum % i == 0): return "NO"

    return "YES"   

while tc > 0:
    tc -= 1
    a,b = map(int, input().split())
    gcd = math.gcd(a, b)

    print(isPrime(gcd))
