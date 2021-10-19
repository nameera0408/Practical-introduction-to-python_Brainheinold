c=0
e9=0
for i in range(1,101):
    p=i*i
    if p%10==4:
        c=c+1
    if p%10==9:
        e9+=1
print(c,e9)
