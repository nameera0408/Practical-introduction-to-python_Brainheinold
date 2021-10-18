temperature = int(input("Enter Temperateture: "))
degree = input("What Units C or F :")

if degree == "F" :
    c = 5/9*(temperature-32)
    print("Your Temperature in Celsius is: ", c)
    
elif degree =="C":
    f= 9/5*temperature + 32
    print("Your temperature in Fahrenheit is: ", f)
    

elif degree != "C" and degree!= "F":
    print("You entered wrong Units")
