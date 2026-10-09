print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tips = float(input("How much tip would you like to give? 10%, 12%, or 15%?\n"))/100
number = int(input("How many people to split the bill?\n"))
calculation =(bill+bill*tips) / number
final_amount= round(calculation,3)
print(f"Each person should pay: {final_amount} $")