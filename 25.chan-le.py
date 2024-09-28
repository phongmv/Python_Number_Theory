def is_odd_number(s):
    s_len = len(s)
    sum = 0


    for i in range(0, s_len - 1):
        if(abs(int(s[i]) - int(s[i+1])) != 2): return "NO"  
        else: sum += int(s[i])
    sum+= int(s[-1])      
    if (sum % 10 == 0): return "YES"     
    return "NO"    

tc = int(input())
while tc > 0:
    tc -= 1
    s = input()
    print(is_odd_number(s)) 