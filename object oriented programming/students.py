class Student():
    def __init__(self, firstName, lastName, major, creditHours, gpa, studentID):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__major = major
        self.__creditHours = creditHours
        self.__gpa = gpa
        self.__studentID = studentID

    def getFirstName(self):
        return self.__firstName
    
    def setFirstName(self, newFirstName):
        self.__firstName = newFirstName
    
    def getLastName(self):
        return self.__lastName
    
    def setLastName(self, newLastName):
        self.__lastName = newLastName
    
    def getMajor(self):
        return self.__major
    
    def setMajor(self, newMajor):
        self.__major = newMajor
    
    def getCreditHours(self):
        return self.__creditHours
    
    def setCreditHours(self, newCreditHours):
        self.__creditHours = newCreditHours
    
    def getGPA(self):
        return self.__gpa
    
    def setGPA(self, newGPA):
        self.__gpa = newGPA
    
    def getStudentID(self):
        return self.__studentID
    
    def getClassLevel(self):
        if self.__creditHours >= 0 and self.__creditHours <= 30:
            return "Freshman"
        elif self.__creditHours >= 31 and self.__creditHours <= 60:
            return "Sophomore"
        elif self.__creditHours >= 61 and self.__creditHours <= 90:
            return "Junior"
        else:
            return "Senior"
        
    def updateCreditHours(self, additionalCreditHours):
        self.__creditHours += additionalCreditHours
    
    def printStudentData(self):
        print("\n")
        print(f"Full Name: {self.__firstName} {self.__lastName}, Student ID: {self.__studentID}")
        print(f"Major: {self.__major}")
        print(f"{self.__creditHours} Credit Hours, {self.__gpa} GPA")