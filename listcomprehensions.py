# list =[expression for item in iterable]
# list =[expression for item in iterable (if conditional)]
# list =[expression (if/else) for item in iterable ]

students = [90,80,60,30,0,12]


passed_students = [student if student >= 30 else "FAILED" for student in students]
passed_student1 = [student for student in students if student >= 80]
passed_student = [student for student in students]

print(passed_student)