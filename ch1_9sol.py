meal_price = eval(input("Enter Price of your meal: "))
tip_percent = eval(input("Enter Tip Percentage"))
tip_amount=(tip_percent/100)*meal_price
print('Total bill:',meal_price+tip_amount,'tip',tip_amount)
