n=int(input())
l=[1,n]
for i in range(2,n):
    if n%i==0:
        l.append(i)
m=[]
s=0
for i in range(2,101):
    m.append(i*i)
print(l)
for i in l:
    if i in m:
        s=1
if s==1:
    print('Not square free')
else:
    print('square free')
