def calculator():
    print("welcome to the python calculator")
    print("mode of operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        choice = input("enter the mode of operation you'd like to perform (1/2/3/4): ")

        if choice in['1','2','3','4']:
            try:
                num1 = float(input("enter your first number: "))
                num2 = float(input("enter your second number: "))
            except ValueError:
                print("invalid input, please enter a numeric input.")
                continue
            
            if choice == '1':
                print(f"{num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"{num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"{num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                if num2 != 0:
                    print(f"{num1} / {num2} = {num1 / num2}")
                else:
                    print("division by zero is invalid")
        else:
            print("invalid choice. Please select a valid mode of operation.")
        
        next_calculation = input("would you like to perform another operation? (yes/no): ").lower()
        if next_calculation != 'yes':
            print("goodbye")
            break

calculator()
