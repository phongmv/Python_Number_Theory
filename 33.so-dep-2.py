def is_pritty_number(number):
    string =  str(number)
    checked_number = string[0] + string[1]
    for i in range(0, len(string) - 1, 2):
        if(checked_number != string[i]+ string[i+1]): return "NO"      
    return "YES"



tc  = int(input())

while tc > 0:
    tc -= 1
    ip = int(input())
    print(is_pritty_number(ip))
    
