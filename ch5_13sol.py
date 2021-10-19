import random
n=int(input())
for i in range(0,10):
    score=0
    r1=random.randint(2,11)
    r2=random.randint(2,11)
    print(r1,'*',r2,':')
    ans=int(input())
    if ans==r1*r2:
        score+=1
print(score)
