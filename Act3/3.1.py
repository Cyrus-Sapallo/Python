
first = input('Enter your first name: ')
last = input('Enter your last name: ')
age = input('Enter your age: ')

#first name and last name
fullname = first + " " + last

# Slicing 
sliced_name = first[:4]

# Formatting 
greeting = "Hello, " + sliced_name +"! Welcome. You are " + age + " years old".format(sliced_name)

print(" ")
print("Full Name:", fullname)
print("Sliced Name:", sliced_name)
print("Greeting Message:", greeting)

