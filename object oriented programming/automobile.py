import datetime

class Automobile():
    #3 principles of object-oriented programming
    #1. Polymorphism
    #2. Inheritance
    #3. Encapsulation

    #define a contructor
    #the constructor defines what happens when we create an automobile
    def __init__(self, make, model, vin, engineSize, owner, year) -> None:
        #assign parameter values
        self.__make = make
        self.__model = model
        self.__vin = vin
        self.__engineSize = engineSize
        self.__owner = owner
        self.__year = year #make year private

    #Create Getter and Setter methods for class attributes
    def getMake(self):
        return self.__make
    
    def getModel(self):
        return self.__model
    
    def getVin(self):
        return self.__vin
    
    def getEngineSize(self):
        return self.__engineSize
    
    def setEngineSize(self, newSize):
        self.__engineSize = newSize

    def getOwner(self):
        return self.__owner
    
    def setOwner(self, newOwner):
        self.__owner = newOwner

    def getYear(self):
        return self.__year
    
    #get automobile age
    def getAge(self):
        #get the current year
        theDate = datetime.datetime.now()
        thisYear = theDate.year
        return thisYear - self.__year

    #print each automobile's data
    def printData(self):
        print(f"{self.__year} {self.__make} {self.__model}")
        print(f"VIN: {self.__vin}, Engine Size: {self.__engineSize}")
        print(f"Owner: {self.__owner}\n")