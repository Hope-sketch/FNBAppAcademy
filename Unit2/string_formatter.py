#Collecting first names, last names, and bio messages using input() function
first_name = (input("Enter your first name: "))
last_name = (input("Enter your last name: "))
bio_message = (input("Enter your bio message: "))

#Creating username by combining first name and last name in lowercase
username = (first_name + last_name).lower()

#Displaying the full name using .title
full_name = (first_name + " " + last_name).title()

#strip leading whitespace from bio message
bio_message = bio_message.lstrip()

#count and display the number of characters in the bio message
bio_length = len(bio_message)

#replace any occurance of "l am" in the bio with 'l'm'using .replace() method
bio_message = bio_message.replace("l am", "I'm")

#displaying all output using f-strings
print(f"Full Name: {full_name}")
print(f"Last name: {last_name}")
print(f"Username: {username}")
print(f"Bio Message: {bio_message}")
print(f"Bio Length: {bio_length}")
