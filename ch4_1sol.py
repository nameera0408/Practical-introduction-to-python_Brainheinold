cm = eval(input("Enter Lenth in Centimeters: "))
if cm < 0:
    print("You Have Entered an Invalid Number")
else:
    inches = cm / 2.54
    print(inches," inches")
