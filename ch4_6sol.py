item = eval(input("How many items do you want to buy:"))

if item < 10:
    print("Total price is: ", item*12)

elif item in range(10,100):
    print("Total price is:", item*10)
elif item >= 100:
    print("Total price is: ",item*7 )
