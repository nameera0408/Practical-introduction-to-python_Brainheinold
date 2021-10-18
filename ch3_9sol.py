hour = eval(input("Enter the the  Current Hour between 1-12 : "))
projected_hour = eval(input("Enter Projected Hour: "))

current_hour = hour + projected_hour

if current_hour > 12:
    current_hour = current_hour % 12


print("New Hour :",current_hour," O'clock")
