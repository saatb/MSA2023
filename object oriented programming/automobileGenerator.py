import automobile

#create an automobile

auto1 = automobile.Automobile("Aston Martin", "Vantage", "5013", 8.0, "John", 2023)
auto2 = automobile.Automobile("Koenigsegg", "One:1", "36905X", 8.0, "Rachel", 2015)

#change auto2's year - can't because we made year private
auto2.__year = 2014

#Change auto1 owner
auto1.setOwner("Jerry")

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


for auto in autoList:
    print(auto.make)
    print(auto.model)
'''

for auto in autoList:
    auto.printData()