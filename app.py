def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def exponent(x, y):
    return x ** y

def print_history(history):
    print("\nCalculation History:")
    for entry in history:
        print(entry)

history = []

while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponent")
    print("6. Show History")
    print("7. Exit")

    choice = input("Enter choice (1/2/3/4/5/6/7): ")

    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = add(num1, num2)
            operation = f"{num1} + {num2} = {result}"

        elif choice == '2':
            result = subtract(num1, num2)
            operation = f"{num1} - {num2} = {result}"

        elif choice == '3':
            result = multiply(num1, num2)
            operation = f"{num1} * {num2} = {result}"

        elif choice == '4':
            result = divide(num1, num2)
            operation = f"{num1} / {num2} = {result}"

        elif choice == '5':
            result = exponent(num1, num2)
            operation = f"{num1} ** {num2} = {result}"

        print(operation)
        history.append(operation)

    elif choice == '6':
        print_history(history)

    elif choice == '7':
        print("Exiting...")
        break

    else:
        print("Invalid input")
