#The Calculator
#using float to collect 2 numbers
number_one = float(input("Enter the first number: "))
number_two = float(input("Enter the second number: "))

#calculate and display:
#Addition
addition = number_one + number_two

#Subtraction
subtraction = number_one - number_two

#Multiplication
multiplication = number_one * number_two

#Division
division = number_one / number_two

#floor division
floor_division = number_one // number_two

#modulus
modulus = number_one % number_two

#Round all results to 2 decimal places
print("Addition: ", round(addition, 2))
print("Subtraction: ", round(subtraction, 2))
print("Multiplication: ", round(multiplication, 2))
print("Division: ", round(division, 2))
print("Floor Division: ", round(floor_division, 2))
print("Modulus: ", round(modulus, 2))

#Handle division by zero error
try:
    division = number_one / number_two
    print("Division: ", round(division, 2))
except ZeroDivisionError:
    print(" please do not divide by zero")

#displaying all results using f-string formatting
print(f"Addition: {round(addition, 2)}")
print(f"Subtraction: {round(subtraction, 2)}")
print(f"Multiplication: {round(multiplication, 2)}")
print(f"Division: {round(division, 2)}")
print(f"Floor Division: {round(floor_division, 2)}")
print(f"Modulus: {round(modulus, 2)}")

