#Create a dictionary of names and scores
studentScores = {"Alice": 87, "Bob": 79, "Jerry": 94, "Sara": 90}

print(studentScores["Bob"])

#declare a car dictionary
car = {"make": "Mercury", "model": "Sable", "year": 1998, "value": 10000, "engine": 3.0}

#get all the values from the student score dictionary
for student in studentScores:
    print(f"{student}: {studentScores[student]}")

print("\n")
#get all the keys and values from the cars dictionary
for key, value in car.items():
    print(f"{key}: {value}")