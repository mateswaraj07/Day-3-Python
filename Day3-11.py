#write a calculator program that has a menu system where it asks for a choise
# from the user (+,-,*,/,!(Factorial)). it should display the output until the user explicitly
# terminated the program by writing exit.
while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Factorial")
    choice = input("Enter your choice (+,-,*,/,!): ")
    if choice == '+':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"Result: {num1 + num2}")
    elif choice == '-':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"Result: {num1 - num2}")
    elif choice == '*':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"Result: {num1 * num2}")
    elif choice == '/':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Error: Division by zero!")
    elif choice == '!':
        import math
        num = int(input("Enter a number to calculate factorial: "))
        fact = 1
        for i in range(1,num+1):
            fact = fact * i
        print(f"Factorial of {num} is {fact}")
    elif choice.lower() == 'exit':
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")