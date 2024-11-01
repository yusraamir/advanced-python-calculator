import sys

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Undefined, division with Zero.")
        return None

def repl():
    print("Welcome to the Advanced Python Calculator!")
    print("Type 'exit' to quit.\n")

    while True:
        # Get user input
        command = input("Enter command (add, subtract, multiply, divide): ").strip().lower()

        # Check if the user wants to exit
        if command == "exit":
            print("Exiting the calculator. Goodbye!")
            break

        # Perform the calculation based on user command
        elif command in {"add", "subtract", "multiply", "divide"}:
            try:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))

                # Call the appropriate function
                if command == "add":
                    result = add(a, b)
                elif command == "subtract":
                    result = subtract(a, b)
                elif command == "multiply":
                    result = multiply(a, b)
                elif command == "divide":
                    result = divide(a, b)

                if result is not None:
                    print(f"Result: {result}\n")
            except ValueError:
                print("Error: Please enter valid numbers.\n")

        # Handle unknown commands
        else:
            print("Unknown command. Please use 'add', 'subtract', 'multiply', 'divide', or 'exit'.")

if __name__ == "__main__":
    repl()