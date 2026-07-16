#input 
first_name = (input("Enter your first name: "))
surname = (input("Enter your surname: "))

#input integar
age = int(input("Enter your age: "))

#input float
favourite_number = float(input("Enter your favourite number: "))

#f-string
print(f"Welcome {first_name} {surname}.")

#uppercase using .upper and in title case using .title
name= first_name + " " + surname
print(name.upper())
print(name.title())

#age in months
age_in_months = age * 12

#favourite number to decimal places
rounded_number= round(favourite_number, 2)
print(f"Your favourite number rounded to 2 decimal places is: {rounded_number}")

#printing all the information using type()
print(type(first_name))
print(type(surname))
print(type(age))
print(type(favourite_number))
