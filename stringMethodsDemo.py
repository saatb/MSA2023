
#capitalize a string
myName = "avyam"
print(myName.capitalize())

print("\n")

#uppercase
print(myName.upper())

print("\n")

#Starts With
print(myName.startswith("avy"))

print("\n")

#ends with
print(myName.endswith("am"))

print("\n")

#find
print(myName.find("a", 2))

sentence = "I have a dog. My dog is cute. Do you want a dog?"

#loop through a string

for character in sentence:
    print(character)

print("\n")

lengthOfString = len(myName)
for index in range(lengthOfString):
    print(myName[index])

print("\n")

dogCount = 0

sentence = "I have a dog. My dog is cute. Do you want a dog?"

#loop
moreDogs = True
startIndex = 0
while moreDogs:
    #find the first instance of dog
    foundIndex = sentence.find("dog", startIndex)
    if foundIndex != -1:
        dogCount += 1
        startIndex = foundIndex + 1
    else:
        moreDogs = False

print(f"Number of Dogs: {dogCount}")