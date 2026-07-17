#Student grade classification program
#Collecting student name and marks for three subjects using input
learner_name = (input("Enter the student's name: "))
subject1_marks = float(input("Enter the marks for subject 1: "))
subject2_marks = float(input("Enter the marks for subject 2: "))
subject3_marks = float(input("Enter the marks for subject 3: "))

#Calculating the average marks
average_marks = (subject1_marks + subject2_marks + subject3_marks) / 3

#Assigning a letter grade: A(80+), B(70-79), C(60-69), D(50-59), F(<50)
if average_marks >= 80:
    grade = 'A'
elif average_marks >= 70:
    grade = 'B'
elif average_marks >= 60:
    grade = 'C'
elif average_marks >= 50:
    grade = 'D'
else:
    grade = 'F'

#Assigning pass status if average is 50 or above, otherwise fail
if average_marks >= 50:
    pass_status = 'Pass'
else:
    pass_status = 'Fail'

#Flag individual subject with below 40 as "needs intervention"
if subject1_marks < 40 or subject2_marks < 40 or subject3_marks < 40:
    intervention_status = "Needs Intervention"

elif subject1_marks == 100 and subject2_marks == 100 and subject3_marks == 100:
    intervention_status = "Excellent Performance"

elif subject1_marks == 100 or subject2_marks == 100 or subject3_marks == 100:
    intervention_status = "Great work! Keep improving the other subjects."

else:
    intervention_status = "No Intervention Needed"

#Displaying formatted report
print("\nStudent Report")
print("======================")
print(f"Name: {learner_name}")
print(f"First subject: {subject1_marks}")
print(f"Second subject: {subject2_marks}")
print(f"Third subject: {subject3_marks}")
print("=======================")
print(f"Average Marks: {average_marks:.2f}")
print(f"Grade: {grade}")
print(f"Pass Status: {pass_status}")
print(f"Intervention Status: {intervention_status}")