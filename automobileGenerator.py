import automobile

#create an automobile

auto1 = automobile.Automobile("Aston Martin", "Vantage", "5013", 8.0, "John")
auto2 = automobile.Automobile("Koenigsegg", "One:1", "36905X", 8.0, "Rachel")

autoList = []
autoList.append(auto1)
autoList.append(auto2)

#print each automobile's info

'''
print(auto1.make)
print(auto1.model)

print("\n")

print(auto2.make)
print(auto2.model)
'''

for auto in autoList:
    print(auto.make)
    print(auto.model)