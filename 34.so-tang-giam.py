def is_ok(n):
    s = str(n)
    if(len(s) < 3): return "NO"
    
    flag = 0
    for i in range(0, len(s) - 1):
        if(s[i] >= s[i + 1]):
            flag = i
            break

    for i in range(flag, len(s) - 1):
        if(s[i] <= s[i +1]): return "NO"

    return "YES"


tc = int(input())

while tc > 0:
    tc -= 1
    ip = int(input())
    print(is_ok(ip))
