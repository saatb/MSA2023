import students
'''
student1 = students.Student("Avyam", "Bansal", "Computer Science", 86, 4.27, "51454")
student2 = students.Student("Joseph", "Kemp", "Civil Engineering", 95, 4.00, "36905")

studentList = []
studentList.append(student1)
studentList.append(student2)
'''

studentDataFile = open("students.csv", "r")
studentList = []
for row in studentDataFile:
    firstName = row[0]
    lastName = row[1]
    major = row[2]
    creditHours = int(row[3])
    gpa = float(row[4])
    studentID = row[5]
    #student = students.Student(row[0], row[1], row[2], int(row[3]), float(row[4]), row[5])
    student = students.Student(firstName, lastName, major, creditHours, gpa, studentID)
    studentList.append(student)

studentDataFile.close()

for student in studentList:
    student.printStudentData()