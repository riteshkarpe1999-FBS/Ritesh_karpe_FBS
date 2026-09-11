# Easy version: Accept marks of 5 subjects for given number of students

num_students = int(input("Enter number of students: "))

for s in range(1, num_students + 1):
    print(f"\n--- Student {s} ---")
    marks = []
    for i in range(1, 6):
        mark = int(input(f"Enter marks for subject {i}: "))
        marks.append(mark)
    print("Marks entered:", marks)


















