#Secret password
password = (input("Please enter your password: "))

#Using .strip() to clean up any accidental spaces
password = password.strip()

#Getting first and last character of the password using indexing
first_character = password[0]
last_character = password[-1]

#printing a hint using f-sting that forces the letters into uppercase
print(f"Your password starts with {first_character.upper()} and ends with {last_character.upper()}.")