print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip2=(bill*(tip/100))
split=((tip2+bill)/people)
final_amount=round(split,2)

print(f"Each person should pay: ${final_amount:.2f}")
244
