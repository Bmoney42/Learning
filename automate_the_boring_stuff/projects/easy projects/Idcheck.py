# Name validation
while True:
    name = input("Enter Your Name: ")
    if name.isalpha():
        break
    else: 
        print("Invalid name! Please use only letters")

# Age validation
while True:
    raw_age = input("Enter your age: ")
    if raw_age.isdigit():                 # make sure it's numbers only
        age = int(raw_age)                # now safe to convert
        if age >= 21:
            print("Can Purchase Alcohol, " + name)
        else:
            print("Not 21, Sorry, " + name)
        break                             # valid input -> exit loop
    else:
        print("Invalid age! Please enter numbers only.")
