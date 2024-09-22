test_case = int(input())

while test_case > 0:
    test_case -=1
    s = input()
    begin  = s[0] + s[1]
    end = s[len(s) - 2] + s[len(s) - 1]
    if(begin == end): print("YES")
    else: print("NO")
