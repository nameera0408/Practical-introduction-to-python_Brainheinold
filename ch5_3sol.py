import math
n=int(input())
s=1
for i in range(2,n+1):
    s=s+(1/i)
    q=s-math.log(n)
print(q)
