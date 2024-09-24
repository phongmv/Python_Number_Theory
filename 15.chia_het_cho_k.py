
a, k , n = map(int, input().split())

flag  = False

for b in range(1,n +1):
   if( ( a +  b) <= n and ( a +  b) % k == 0): 
     flag = True
     print(b, end=" ")
    
print()
if not flag:
    print(-1)

