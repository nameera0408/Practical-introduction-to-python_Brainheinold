year = eval(input("Enter a Year: "))
for years in range(1600,year):
    if years % 4 == 0 or years % 100 == 0 and years % 400 == 0:
        print( years)
