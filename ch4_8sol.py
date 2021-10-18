year = int(input("Enter Year To Check if its a leap year: "))

if year % 4 == 0 or year % 100 != 0 and year % 400 == 0:

    print(year," is a leap year")

else:
    print(year,"is not a leap Year"
