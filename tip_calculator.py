print("Welcome to the tip calculator.")
bill=float(input("What was the total bill? $"))
tip=int(input("What percent tip would you like to give? 10, 12 or 15?"))
friends=int(input("How many people to split the bill?"))
tip_percentage=(tip/100)*bill
total_tip=bill+tip_percentage
each=total_tip/friends
final_amount=round(each,2)
print(f"Each person should pay: ${final_amount}")
