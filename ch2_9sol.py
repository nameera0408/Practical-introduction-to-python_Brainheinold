num = eval(input("How many Fibonacci Numbers do you want to Print: "))
first_number = 0
second_number = 1
print(first_number)
print(second_number)
for i in range(2,num):

    next_number =first_number + second_number
    first_number = second_number
    second_number = next_number

    print(next_number)

