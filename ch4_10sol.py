import random

print('Question')
m=random.randint(1,10)
n=random.randint(1,10)
print(m,'*',n,'=')
q=int(input())
if m*n==q:
    print('You are right')
else:
    print('You are wrong')
