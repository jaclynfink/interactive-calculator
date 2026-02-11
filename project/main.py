def get_number(user_input):
    while True:
        value = input(user_input).strip()
        try:
            if "." in value:
                return float(value)
            else:
                return int(value)
        except ValueError:
            print("ERROR: Invalid number.")

def parse_number(value: str): ## for pytest, to test get_number logic without user input
    try:
        number = float(value)
        return int(number) if number.is_integer() else number
    except ValueError:
        raise ValueError("ERROR: Invalid number.")


def calculate(operation, num1, num2): ## addition, subtraction, multiplication, and division
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            raise ZeroDivisionError("ERROR: Cannot divide by zero.")
        return num1 / num2
    else:
        raise ValueError("ERROR: Invalid operation.")


def main():
    print("\nInteractive Calculator")
    print("Available operations:")
    print("+  -  *  /")
    print("\nPress q to quit")

    while True: ## Read-Eval-Print Loop
        operation = input("\nEnter operation: ").strip()

        if operation.lower() == "q":
            break

        if operation not in ["+", "-", "*", "/"]:
            print("ERROR: Invalid operation. Please choose +, -, *, /, or q.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        try:
            result = calculate(operation, num1, num2)
            print(f"{result}")
        except ZeroDivisionError as e:
            print(f"ERROR: {e}")
        except Exception as e:
            print(f"ERROR: {e}")


if __name__ == "__main__":
    main()
