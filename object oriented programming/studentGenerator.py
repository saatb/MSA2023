import students
from datetime import datetime
'''
student1 = students.Student("Avyam", "Bansal", "Computer Science", 86, 4.27, "51454")
student2 = students.Student("Joseph", "Kemp", "Civil Engineering", 95, 4.00, "36905")

studentList = []
studentList.append(student1)
studentList.append(student2)
'''


'''
function to write to error log file
input: error message
output: none
'''
def writeToErrorLog(message):
    #open log file
    try:
        logFile = open("errorLog.txt", "a")
        logFile.write(f"{datetime.now()}: {message}")
        logFile.close()
    except Exception as err:
        print(err)
        return
    
    return


studentDataFile = open("students.csv", "r")
studentList = []
for row in studentDataFile:
    row = row.strip("\n")
    dataList = row.split(",")
    if dataList[0] == "first_name":
        continue
    firstName = dataList[0]
    lastName = dataList[1]
    major = dataList[2]
    creditHours = int(dataList[3])
    try:
        gpa = float(dataList[4])
        studentID = dataList[5]
    except Exception as err:
        #if error in format then write a message to a log file
        writeToErrorLog(f"Error in data: {row}, {err}\n")
        index = dataList[4].find(".")
        gpa = float(dataList[4][index - 1: index + 2])
        studentID = dataList[4][index + 3: ]
    #student = students.Student(row[0], row[1], row[2], int(row[3]), float(row[4]), row[5])
    student = students.Student(firstName, lastName, major, creditHours, gpa, studentID)
    studentList.append(student)

studentDataFile.close()

for student in studentList:
    student.printStudentData()

