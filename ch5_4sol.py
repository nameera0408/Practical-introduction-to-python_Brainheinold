s=0
q=0
for i in range(1,2001):
    if i%2==0:
        q=q+i
    else:
        s=s+i
print(s-q)
