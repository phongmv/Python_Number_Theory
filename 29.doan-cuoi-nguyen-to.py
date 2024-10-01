


def is_prime(number):
    if number < 2:
        return "NO"
    for i in range(2, number): 
        if number % i == 0:
            return "NO"
    return "YES"


def is_last_prime_number(string):
    return int(string[-4:])


tc = int(input())

while tc >0: 

    tc -= 1
    s = input()
    print(is_prime(is_last_prime_number(s)))