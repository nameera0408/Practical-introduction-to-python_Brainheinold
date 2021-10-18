width = eval(input("Enter Width: "))
height = eval(input("Enter Height: "))

for i in range(0,width*height,1):
    print("")
    for j in range(0+i,width+i,1):
        print(j%10,end="")
