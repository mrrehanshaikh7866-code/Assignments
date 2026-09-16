# Input the number of students
num_students = int(input("Enter the number of students: "))

class_total = 0

# Loop for each student
for student in range(1, num_students + 1):

    student_total = 0

    print(f"\nEnter scores for Student {student}:")

    # Input 5 test scores
    for test in range(1, 6):
        score = float(input(f"Enter score for Test {test}: "))
        student_total += score

    # Calculate average
    student_average = student_total / 5

    print(f"Average score of Student {student}: {student_average:.2f}")

    class_total += student_total

# Calculate class average
overall_average = class_total / (num_students * 5)

print(f"\nOverall average score of the class: {overall_average:.2f}")