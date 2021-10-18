import random
name=input('Enter your name:')
x=random.randint(1,50)
print(name*x)
#Or (By using for loop):
for i in range(0,x):
  print(name,end=' ')
