print("Welcome To The Tip Calculator")
total_bill = float(input("What Was the total bill: $"))
tip_percent = int(input("What would you Like to tip: (12, 15, or 20%) "))
total_bill_with_tip = (total_bill * (tip_percent/100)) + (total_bill)
number_of_people = int(input("how many people to split the bill: "))

individual_bill = total_bill_with_tip / number_of_people

final_amount = round(individual_bill, 2)

print(f"Each Person is Expected To Pay ${final_amount} Each")
