grade_table = {"A": 4, "B": 3, "C": 2, "D": 1}
total_grade_points = 0
total_credits = 0
print("----------GPA Calculator----------\n\n")
num_courses = int(input("Enter number of courses: "))

for i in range(num_courses):
  grade = input("Enter the letter grade for course(in UPPERCASE) " + str(i + 1) + ": ")
  credits = int(input("Enter the number of credits for course " + str(i + 1) + ": "))
  total_grade_points += grade_table[grade] * credits
  total_credits += credits

GPA = total_grade_points / total_credits

print("GPA:", GPA)
