n=10
m=list(map(int,input().strip().split()))[:n]
m.sort()
x=1
for i in m:
    if i>99:
        x=0
if x==0:
    print('A value over 100 has been entered!')
print('highest score:',m[-1])
print('lowest score:',m[0])
sum=0
for i in m:
    sum+=i
print('Average score:',sum/10)
print('second largest score',m[-2])
m.remove(m[-1])
m.remove(m[-2])
sum1=0
for i in m:
  sum1+=i
print('average by removing least two scores:',sum1/n)
