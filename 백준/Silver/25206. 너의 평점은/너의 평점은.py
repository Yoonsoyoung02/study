
grade_to_point = {
    "A+": 4.5, "A0": 4.0,
    "B+": 3.5, "B0": 3.0,
    "C+": 2.5, "C0": 2.0,
    "D+": 1.5, "D0": 1.0,
    "F": 0.0
}


subjects = []
for _ in range(20):
    data = input().strip().split()
    subject_name, credit, grade = data[0], float(data[1]), data[2]
    subjects.append((credit, grade))

weighted_sum = 0.0
credit_sum = 0.0

for credit, grade in subjects:
    if grade == "P":
        continue
    weighted_sum += credit * grade_to_point[grade]
    credit_sum += credit


if credit_sum > 0:
    major_gpa = weighted_sum / credit_sum
    print(f"{major_gpa:.6f}")
else:
    print("0.000000")
