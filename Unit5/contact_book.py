#Command-line contact book
#Storing contacts as a list of dictionaries, each with keys: name, phone, email
#Implementent an add_contact(name) function that appends a new dictionary to the list
import email


contacts = []

def add_contact(name, phone, email):
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    return contact

#Implement a search_contact(name) function that searches for a contact by name and returns the contact details if found, or a message indicating that the contact was not found.
search_name = input("Enter the name of the contact to search: ")

def search_contact(name):
    for contact in contacts:
        if contact["name"] == name:
            return contact
    return "Contact not found."

#Implement a delete_contact(name) function that searches for a contact by name and removes it from the list if found, or returns a message indicating that the contact was not found.
def delete_contact(name):
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            return f"Contact {name} deleted."
    return "Contact not found."

#implement a view_all() function that displays all contacts in the list.
def view_all():
    if not contacts:
        return "No contacts found."
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

#Using a while loop menu to let the user choose an action (1=Add, 2=Search, 3=Delete, 4=View All, 5=exit) and call the appropriate function based on the user's choice.
while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All Contacts")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_name = input("Enter contact name: ")
        add_phone = input("Enter contact phone: ")
        add_email = input("Enter contact email: ")
        
        add_contact(add_name, add_phone, add_email)
        
        print(f"Contact {add_name} added.")

    elif choice == "2":
        search_name = input("Enter the name of the contact to search: ")
        result = search_contact(search_name)
        if isinstance(result, dict):
            print(f"Contact found: Name: {result['name']}, Phone: {result['phone']}, Email: {result['email']}")
        else:
            print(result)

    elif choice == "3":
        delete_name = input("Enter the name of the contact to delete: ")
        result = delete_contact(delete_name)
        print(result)

    elif choice == "4":
        view_all()

    elif choice == "5":
        print("Exiting Contact Book.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")