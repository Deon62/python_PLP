print("...Welcome to Deon calculator!...")
print()
while True:
    print("...Please enter the first number...")
    num1 = int(input("number 1: "))
    print()
    print("...Please enter the second number...")
    num2 = int(input("number 2: "))
    print()
    print("...Please enter the mathematical operation you want to perform...")
    print()
    operation = input("operation: ")
    if operation == "+":
            
        print(f"{num1} + {num2} = {num1 + num2}")

    elif operation == "-":
        print(f"{num1} - {num2} = {num1 - num2}")

    elif operation == "*":
            print(f"{num1} * {num2} = {num1 * num2}")

    elif operation == "/":
        print(f"{num1} / {num2} = {num1 / num2}")

    else:
        print("...Invalid operation...")

#you want to continue?
    print("...Do you want to continue?...")
    print("...Please enter 'yes' or 'no'...")
    answer = input("answer: ")
    if answer == "yes":
        continue
    elif answer == "no":
        print("...Thank you for using Deon calculator...")
        break
