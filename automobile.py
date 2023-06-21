class Automobile():
    #define a contructor
    #the constructor defines what happens when we create an automobile
    def __init__(self, make, model, vin, engineSize, owner) -> None:
        #assign parameter values
        self.make = make
        self.model = model
        self.vin = vin
        self.engineSize = engineSize
        self.owner = owner