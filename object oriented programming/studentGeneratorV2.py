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

'''
function to return list of Student objects
Input: none
Output: list of Student objects
'''
def loadStudents():
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
    return studentList

'''
function to convert student object to student dictionaries
Input: list of Student objects
Output: list of student dictionaries
'''

def studentToDictionary(studentList):
    #create a list to store the dictionaries
    studentDictionaryList = []
    for student in studentList:
        studentDictionary = {}
        #set keys and values for first name, last name, ID, major, gpa, and class level
        studentDictionary["firstName"] = student.getFirstName()
        studentDictionary["lastName"] = student.getLastName()
        studentDictionary["studentID"] = student.getStudentID()
        studentDictionary["major"] = student.getMajor()
        studentDictionary["class"] = student.getClassLevel()
        studentDictionary["gpa"] = student.getGPA()
        studentDictionaryList.append(studentDictionary)
    return studentDictionaryList


'''
function to get student dictionaries
Input: none
Output: list of student dictionaries
'''

def getStudentDictionaries():
    studentList = loadStudents()
    studentDictionaries = studentToDictionary(studentList)
    return studentDictionaries

