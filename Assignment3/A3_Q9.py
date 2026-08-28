# Program to calculate grade based on 5 subject marks

# Input marks
marks = []
for i in range(5):
    mark = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

# Calculate total and percentage
total = sum(marks)
percentage = total / 5

# Determine grade
if percentage >= 60:
    grade = "First Class"
elif percentage >= 50:
    grade = "Second Class"
elif percentage >= 40:
    grade = "Pass Class"
else:
    grade = "Fail"

# Display result
print("\nTotal Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)


















