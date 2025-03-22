def div(a, b): #divide
    if b == 0:
        print("Denominator cannot be zero.")
        return None
    return a / b

def exp(a, b): #exponentiation
    
    return a ** b

def rem(a, b): #remainder
    if b == 0:
        print("Denominator cannot be zero.")
        return None
    return a % b

def summ(a, b): #summation

    if b <= a:
        print("The second number must be greater than the first number.")
        return None
    return sum(range(a, b + 1))

def display_menu(): #choices
   
    print("Menu:")
    print("[D] - Divide")
    print("[E] - Exponentiation")
    print("[R] - Remainder")
    print("[F] - Summation")
    print("[Q] - Quit")

def main(): 
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip().upper()

        if choice == "Q":
            print("Exiting the program.")
            break

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input.")
            continue

        if choice == "D":
            result = div(num1, num2)
        elif choice == "E":
            result = exp(num1, num2)
        elif choice == "R":
            result = rem(num1, num2)
        elif choice == "F":
            result = summ(num1, num2)
        else:
            print("Please try again.")
            continue

        if result is not None:
            print(f"Result: {result}")

if __name__ == "__main__":
    main()