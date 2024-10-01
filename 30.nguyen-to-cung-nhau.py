import math

a, b = map(int, input().split())


def is_dub_prime_numbers(a,b):
    cnt  = 1
    for i in range(10 ** (b-1), 10 ** b):
        if(math.gcd(a, i) == 1): 
            cnt += 1
            print(i, end=" ")
            if(cnt > 10): 
                print()
                cnt = 1        


is_dub_prime_numbers(a,b)
