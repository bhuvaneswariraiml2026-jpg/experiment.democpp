#student Mark,percentage and grade
name=input("Enter student name:")
n=int(input("Enter number of subjects:"))
total=0
for i in range(n):
    mark=int(input(f"Enter mark for subject {i+1}:"))
    total += mark
percentage = total / n
if percentage >= 90:
    grade = "A+"
    performance = "Outstanding"
elif percentage >= 80:
    grade = "A"
    performance = "Excellent"
elif percentage >= 70:
    grade = "B"
    performance = "Very Good"
elif percentage >= 60:
    grade = "C"
    performance = "Good"
else:
    grade = "D"
    performance = "Poor"
rmance}")
print(f"Student Name: {name}")
print(f"Percentage: {percentage}")
print(f"Grade: {grade}")
print(f"Performance: {perfo