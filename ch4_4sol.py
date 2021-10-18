credits_taken = eval(input("Emter the number of credit taken: "))

if credits_taken <= 23:
    print("You are a fresh man")
elif credits_taken >= 24 and credits_taken <= 53:
    print("You are a sophormore")
elif credits_taken >= 54 and credits_taken <= 83:
    print("You are a Junior")
elif credits_taken >= 84:
    print("Congrats You are a Senior")
