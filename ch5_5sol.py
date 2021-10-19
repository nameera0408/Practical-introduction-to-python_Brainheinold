n=int(input())
l=[1,n]
for i in range(2,n):
    if n%i==0:
        l.append(i)
sum=0
for i in l:
    sum+=i
print(sum)
