def is_luckyly_number(s):
    if(s.endswith('86')): return "YES"
    return "NO"

tc = int(input())
while tc >0:
    tc-=1    
    s = input()
    print(is_luckyly_number(s))