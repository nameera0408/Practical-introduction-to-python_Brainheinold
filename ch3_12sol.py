n=int(input('Enter your number'))
factorial=1
if n==1:
  print(1)
if n==0:
  print('Factorial to the number doesnt exist')
else:
  for i in range(1,n+1):
    factorial=factorial*i
  print(factorial)
