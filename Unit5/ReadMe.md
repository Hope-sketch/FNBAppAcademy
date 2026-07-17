# Unit 5 – Selection of Tasks

Welcome to **Unit 5** of the **FNB App Academy – Introduction to Python** course.

This unit introduces decision-making, functions, and repetition using `while` loops. These concepts are essential for creating interactive applications that continue running until the user decides to exit.

---

#  Projects

##  ScoreTracker.py

### Real-world Problem

Arcade games and online leaderboards need a way to continuously accept player scores and determine whether a new high score has been achieved.

### Solution

This program repeatedly asks the user to enter a score until they choose to stop. It then checks whether the score qualifies as a high score and displays the appropriate message.

### Concepts Practised

- `while True`
- `break`
- `if`, `elif`, `else`
- User Input
- Integer Conversion
- String Methods (`.strip()`, `.lower()`)

---

##  contact_book.py

### Real-world Problem

Managing contact information is a common feature in many applications, from smartphones to customer management systems. Instead of storing just one contact, applications need an efficient way to add, search, display, and remove multiple contacts.

### Solution

This application stores contacts as a **list of dictionaries**, allowing users to:

- Add new contacts
- Search for contacts by name
- Delete existing contacts
- View all saved contacts

The program runs through a menu-driven interface until the user chooses to exit.

### Concepts Practised

- Lists
- Dictionaries
- Functions
- `while` Loops
- `for` Loops
- Searching Data
- CRUD Operations (Create, Read, Delete)

---

# Python vs C# Perspective

This was probably the unit where I compared Python to C# the most.

The idea of creating functions and calling them felt exactly like C#. The biggest difference was understanding that in Python, functions can work directly with lists and dictionaries without needing to build separate classes for small projects.

| Python | C# |
|---------|------|
| `def add_contact()` | `void AddContact()` |
| `while True:` | `while(true)` |
| `break` | `break` |
| `return` | `return` |
| List of Dictionaries | `List<Contact>` or `List<Dictionary<string,string>>` |

One lesson I learned the hard way was that **creating a function and calling a function are two different things**. At first, I accidentally treated my function like a dictionary. Fixing that mistake helped me better understand how functions work in Python.

---

#  What I Learned

By completing this unit, I learned how to:

- Write reusable functions
- Build menu-driven applications
- Use infinite loops responsibly
- Search through collections
- Store structured information using lists of dictionaries

Perhaps the biggest lesson was that programming becomes much easier once you stop trying to memorise syntax and instead focus on understanding what each piece of code is supposed to accomplish.

---

##  A Lesson I Learned in contact_book.py

While building this project, I made a mistake because I was thinking in C# rather than Python.

I correctly created an `add_contact()` function:

```python
def add_contact(name, phone, email):
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
```

However, when calling the function, I wrote:

```python
add_contact(add_name, add_phone, add_email)
contacts.append(add_contact)
```

### Why this is wrong

The `add_contact()` function already creates the contact dictionary and appends it to the `contacts` list.

By writing:

```python
contacts.append(add_contact)
```

I was trying to append the **function itself** instead of a contact.

### Thinking in C#

This mistake made sense once I compared it to C#.

Imagine the following method:

```csharp
public void AddContact(string name, string phone, string email)
{
    Contact contact = new Contact
    {
        Name = name,
        Phone = phone,
        Email = email
    };

    contacts.Add(contact);
}
```

The method already adds the contact to the list.

You would simply call:

```csharp
AddContact(name, phone, email);
```

You would **not** write:

```csharp
contacts.Add(AddContact);
```

because `AddContact` is the method, not the contact object.

Python works the same way.

### Correct solution

```python
if choice == "1":
    add_name = input("Enter contact name: ")
    add_phone = input("Enter contact phone: ")
    add_email = input("Enter contact email: ")

    add_contact(add_name, add_phone, add_email)

    print(f"Contact {add_name} added.")
```

### What I learned

Coming from C#, I naturally compared Python functions to C# methods.

This project taught me that once a function is responsible for creating and storing an object, I only need to call the function. I do **not** need to manually append the function itself to the list.

This was a good reminder that although Python and C# have different syntax, many of the programming concepts are the same.
