def is_ok(s):   
    for c in s:
        if c not in ["0", "1", "2"]:
            return "NO"
    return "YES"

tc = int(input())

while tc > 0:
    tc -= 1
    ip = input()
    print(is_ok(ip))
