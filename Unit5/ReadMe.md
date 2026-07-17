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
