print('enter a word')
x = input()
#vowels that is gonna be counted
vowels = ["a", "e", "i", "o", "u"]
#is default counter
numbervowels = 0
numbercons = 0
space = 0

for char in x:
    #counter of vowels
    if char in vowels:
        numbervowels +=1
    #counter of consonant
    elif char not in vowels:
        numbercons += 1
    #counter of space
    elif char == " ":
        space +=1
#output
print ("vowels: ", {numbervowels})
print ("consonant: ", {numbercons})
print ("space: ", {space})








