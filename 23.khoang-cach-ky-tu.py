def calc_distace(a, b):
    
    for i  in range(1, len(a)):
        abs_a = abs(ord(a[i]) - ord(a[i-1]))
        abs_b = abs(ord(b[i]) - ord(b[i-1]))
        if(abs_a != abs_b): return "NO"
    
    return "YES"         

def reverse_string(s):
    return s[::-1]

tc = int(input())
while tc >0:
    tc -= 1
    string = input()
    rv_string = reverse_string(string)
    
    print(calc_distace(string, rv_string))
    
    

