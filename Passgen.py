import random
length=int(input("Password length"))
nopass=int(input("no of passwords required"))
chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="!~@#$%^&*/.,:';"
password=''
number=int(input("numbers required(1/0)")) # if you need numbers in your Password enter 1(True) else 0(False)
symbol=int(input("symbols required(1/0)"))  # if you need symbols in your Password enter 1(True) else 0(False)
for l in range(nopass):
    password=''
    for i in range(length):
        if number==1 & symbol==1:
            password+=random.choice(chars+numbers+symbols)
        elif number==1 & symbol==0:
            password+=random.choice(chars+numbers)
        elif number==0 & symbol==1:
            password+=random.choice(symbols+chars)
        else:
            password+=random.choice(chars)
    print(password)
