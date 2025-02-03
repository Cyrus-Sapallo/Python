print('enter a word')
x = input()
vowels = ["a", "e", "i", "o", "u"]

numbervowels = 0
numbercons = 0
space = 0
for char in x:
    if char in vowels:
        numbervowels +=1
    elif char not in vowels:
        numbercons += 1
    elif char == " ":
        space +=1
print ("vowels: ", {numbervowels})
print ("consonant: ", {numbercons})
print ("space: ", {space})








