print("Hello Wolcome To Soufiane Coffee")
name = input("what is your name\n")

if name.startswith("m"):
    print("your not wolcome here evil " + name + "!!!\nget out of here NOW!!!!")
    exit()
    
else:
    print("Hello " + name + " your wolcome here and thanks for comming")

print("this menu about drink let's chose:")

menu = ("tea = 5DH\njuice = 10DH\ncoffee = 8DH\ncappucino = 13DH\nespresso = 12DH\nlatte = 15DH\n")
order = input("What would you like \n" + menu +"\n")
if order == "tea" or order == "juice" or order == "coffee" or order == "cappucino" or order == "espresso" or order == "latte":
    print("Okey we gonna serve you now")
else:
    print("SORRY but we don't have this order here i hope you to command another thing")
    exit()
quantity = input("how many cop " + order + " would you like ")
price = input("the your price\n")
if order == "tea":
    price = 5
elif order == "juice":
    price = 10
elif order == "latte":
    price = 15
    cream = input("do you want wipped cream ?")
    if cream == "yes":
        print("you latte would be 18DH")
    else:
        print("you latte would be on you in 2 minutes")
elif order == "coffee":
    price = 8
elif order == "cappucino":
    price = 13
elif order == "espresso":
    price = 12
else:
    print("sorry you have to pay")
print(price)
    