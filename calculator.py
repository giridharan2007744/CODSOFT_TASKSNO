
def get_number(prompt):
   
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a valid number (e.g. 5 or 3.2).")


def calculate(num1, num2, operation): 
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return None
        return num1 / num2
    else:
        print("Error: Invalid operation choice.")
        return None


def main():
    print("=== Simple Calculator ===")
    print("Operations available: + - * /")

    while True:
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        operation = input("Choose an operation (+, -, *, /): ").strip()

        result = calculate(num1, num2, operation)

        if result is not None:
            # Show as an integer if it's a whole number, else show decimal
            if result == int(result):
                result = int(result)
            print(f"Result: {num1} {operation} {num2} = {result}")

        again = input("\nDo you want to perform another calculation? (y/n): ").strip().lower()
        if again != 'y':
            print("Thank you for using the calculator. Goodbye!")
            break
        print()  # blank line for readability


if __name__ == "__main__":
    main()