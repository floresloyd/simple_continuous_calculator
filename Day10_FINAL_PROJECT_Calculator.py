def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    is_continuing = True
    num1 = float(input("Enter your first number: "))
    while is_continuing:
        for symbol in operations:
            print(symbol)
        user_input = str(input("What operation do you want to perform?: "))
        num2 = float(input("Enter your second number: "))
        selected_function = operations[user_input]
        result = selected_function(num1, num2)
        print(f"{num1} {user_input} {num2} = {result}")

        how_to_continue = input(f"\n"
                                f" Type 'y' to continue calculating with {result} \n "
                                f"Type 'n' to start a fresh calculation \n "
                                f"Type 'q' to quit \n"
                                f" Input: "
                                )
        if how_to_continue == 'y':
            num1 = result
        if how_to_continue == 'n':
            is_continuing = False
            calculator()  # Recursive call
        if how_to_continue == 'q':
            is_continuing = False
            print("Program will terminate. Thank you for using this calculator")


calculator()
