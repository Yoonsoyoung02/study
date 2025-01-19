grade_to_point = {
    "A+":4.5,"A0":4.0,
    "B+":3.5,"B0":3.0,
    "C+":2.5,"C0":2.0,
    "D+":1.5,"D0":1.0,
    "F":0.0
    }

credit_sum = 0.0
total_cg = 0.0

for _ in range(20):
    subject_name, credit, grade = input().split()
    credit = float(credit)
    if grade == 'P':
        continue
    total_cg = total_cg + credit*grade_to_point[grade]
    credit_sum += credit

print(total_cg/credit_sum)