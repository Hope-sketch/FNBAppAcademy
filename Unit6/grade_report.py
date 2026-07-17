# Grade Report Generator

# Store at least 5 students as a list of dictionaries
students = [
    {
        "name": "Hope",
        "maths": 81,
        "english": 69,
        "science": 75
    },
    {
        "name": "John",
        "maths": 60,
        "english": 80,
        "science": 70
    },
    {
        "name": "Sarah",
        "maths": 95,
        "english": 88,
        "science": 91
    },
    {
        "name": "Peter",
        "maths": 45,
        "english": 58,
        "science": 62
    },
    {
        "name": "Lebo",
        "maths": 72,
        "english": 67,
        "science": 78
    }
]

# Store processed results
results = []

# Used to calculate class statistics
averages = []

# Loop through every student
for student in students:

    # Calculate average
    average = (
        student["maths"] +
        student["english"] +
        student["science"]
    ) / 3

    averages.append(average)

    # Determine grade
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    # Determine pass/fail
    if average >= 50:
        status = "Pass"
    else:
        status = "Fail"

    # Store results
    results.append({
        "name": student["name"],
        "average": round(average, 2),
        "grade": grade,
        "status": status
    })

# Calculate class statistics
class_average = round(sum(averages) / len(averages), 2)
highest_mark = max(averages)
lowest_mark = min(averages)

# Display report
print("\n===== CLASS REPORT =====")

for result in results:
    print("----------------------------")
    print(f"Name: {result['name']}")
    print(f"Average: {result['average']}")
    print(f"Grade: {result['grade']}")
    print(f"Status: {result['status']}")

print("\n===== CLASS STATISTICS =====")
print(f"Class Average: {class_average}")
print(f"Highest Average: {highest_mark:.2f}")
print(f"Lowest Average: {lowest_mark:.2f}")

# Search by student name
while True:

    search = input("\nEnter a student's name to search (or type 'exit'): ").strip()

    if search.lower() == "exit":
        print("Program ended.")
        break

    found = False

    for result in results:
        if result["name"].lower() == search.lower():

            print("\nStudent Found")
            print("----------------------")
            print(f"Name: {result['name']}")
            print(f"Average: {result['average']}")
            print(f"Grade: {result['grade']}")
            print(f"Status: {result['status']}")

            found = True
            break

    if not found:
        print("Student not found.")