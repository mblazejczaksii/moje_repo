from calculator.logo import logo

print(logo)
def adding(n1, n2):
    return n1 + n2


def subtraction(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculator():
    operations = {
        '+': adding,
        '-': subtraction,
        '*': multiply,
        '/': divide
    }
    n1 = float(input("What's the first number?"))

    for key in operations.keys():
        print(key)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation...")
        n2 = float(input("What's the next number?"))
        calculation = operations[operation_symbol]
        answer = calculation(n1, n2)
        print(f"{n1} {operation_symbol} {n2} = {calculation(n1, n2)}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation") == 'y':
            n1 = answer
        else:
            print(f"Last result is {answer}")
            should_continue = False
            calculator()


calculator()
