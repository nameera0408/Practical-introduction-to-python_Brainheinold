n=int(input('Enter hour:))
m=int(input('am(1) or pm(0)'))
h=int(input('how many hours ahead')
x=n+h
if m==1:
      if x>12:
        x=x-12
        print(x,'pm')
      else:
        print(x,'pm')
else:
      if x>12:
        x=x-12
        print(x,'am')
      else:
        print(x,'am')
