temp_celcuis = eval(input("Enter temperature in Celcuis: "))
absolute_zero = -273.15
if temp_celcuis < absolute_zero:
    print("Temperature is invalid and below freezing point")
elif temp_celcuis ==   absolute_zero:
    print("The temperature is absolute zero")
elif temp_celcuis <= 0 :
    print("Temperature is below freezing point")
elif temp_celcuis == 0:
    print("Temperatur is at freezing point")
elif temp_celcuis > 0 and temp_celcuis < 100:
    print("Temperature is in normal range")
elif temp_celcuis == 100:
    print("The temperature is at boiling point")
elif temp_celcuis > 100:
    print("The temperature is above boiling point")
