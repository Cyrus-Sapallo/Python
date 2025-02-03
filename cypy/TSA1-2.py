print('enter a word')
x = input()
sum = 0
#x is the input
for digit in x:
    sum +=int (digit)
    #the sum resulted from +=int(digit)
print ("you out in:", x)
print("sum of digits", {sum})
