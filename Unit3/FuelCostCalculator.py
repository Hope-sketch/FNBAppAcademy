#The South African Fuel cost calculator
#Input km driver wants

kilometers = float(input("Enter the distance you want to travel in kilometers: "))

#Current fuel price per liter in South Africa
fuel_per_liter = float(input("Enter the current fuel price per liter in South Africa (in R): "))

#Assuming car uses exactly 1 liter of fuel for every 10 km, (Formula: liters_needed = km/10)
fuel_needed = kilometers / 10

#Calculate the total cost of fuel needed
total_cost = fuel_needed * fuel_per_liter

#Using type casting to ensure numbers work, use round() 
total_cost_rounded = round(total_cost, 2)

#Output the total cost of fuel needed
print(f"\nFuel needed: {fuel_needed} liters")
print(f"Total fuel cost: R{total_cost_rounded}")
