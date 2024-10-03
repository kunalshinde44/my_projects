# Simple calculator in Python

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    # Get user input
    operation = input("Enter choice (1/2/3/4): ")

    if operation in ['1', '2', '3', '4']:
        # Get numbers from user
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if operation == '1':
            print(f"The result of {num1} + {num2} is {num1 + num2}")
        elif operation == '2':
            print(f"The result of {num1} - {num2} is {num1 - num2}")
        elif operation == '3':
            print(f"The result of {num1} * {num2} is {num1 * num2}")
        elif operation == '4':
            if num2 != 0:
                print(f"The result of {num1} / {num2} is {num1 / num2}")
            else:
                print("Error! Division by zero.")
    else:
        print("Invalid input, please choose a valid operation.")

# Call the calculator function
calculator()
