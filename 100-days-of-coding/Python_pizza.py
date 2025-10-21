print(" Welcome To Python Pizza Deliveries")

total_price = 0


# small pizza is 15
# medium pizza is 20
# large pizza is 25
# pepperoni is extra 2 for small/medium and 3 for large
# extra cheese is 1

size = input("What size pizza do you want? S, M or L: ")
if size == "S" or size == "s":
    print("\nYou want a Small pizza, that will be $15")
    total_price += 15
elif size == "M" or size == "m":
    print("\nYou want a Medium pizza, that will be $20")
    total_price += 20
elif size == "L" or size =="l":
    print("\nYou want a Large pizza, that will be $25")
    total_price += 25
else:
    print(" please choose between S, M or L Pizza")

pepperoni = input("Do you want pepperoni on your pizza Y or N: ")
if pepperoni == "Y" or pepperoni == "y":
    if size == "m" or size == "M":
        print("We added Pepperoni To Your Medium Pizza")
    elif size == "s" or size == "S":
        print("We added Pepperoni To Your small Pizza")
        total_price += 2
    else:
        print("We added Pepperoni To Your Large Pizza")
        total_price += 3
else:
    print("No pepperonis for you")
        

extra_cheese =  input("Do you want extra cheese? Y or N: ")
if extra_cheese == "y" or extra_cheese == "Y":
    print("We Added Extra Cheese For $1")
    total_price += 1

print(f"Your total price is ${total_price}")

