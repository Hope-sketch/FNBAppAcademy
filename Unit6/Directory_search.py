#Creating a dictionary
contacts = {
    "Khensani": "0823908899",
    "Lungi": "0820989000",
    "Nina": "0888640954"
}

#User input
search_name = input("Enter a friend's name: ")

#using if statement
if search_name in contacts:

    number = contacts[search_name]

    print(f"Found! {search_name}'s number is {number}")

else:

    print("Contact not found.")