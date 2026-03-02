print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tipPercent = tip / 100
tipAmount = bill * tipPercent
totalBill = bill + tipAmount
per_person = totalBill / people

print(f"Each person should pay: ${per_person:.2f}")
print(f"Each person should pay: ${int(per_person)}")
