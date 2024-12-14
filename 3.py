def calculator():
    print("Калькулятор")
    a = float(input("Введіть перше число (a): "))
    b = float(input("Введіть друге число (b): "))
    operation = input("Виберіть операцію (+, -, *, /): ")
    if operation == "+":
        result = a + b
        print(f"{a} + {b} = {result}")
    elif operation == "-":
        result = a - b
        print(f"{a} - {b} = {result}")
    elif operation == "*":
        result = a * b
        print(f"{a} * {b} = {result}")
    elif operation == "/":
        if b == 0:
            print("Ділення на нуль!")
        else:
            result = a / b
            print(f"{a} / {b} = {result}")
    else:
        print("Некоректна операція. Будь ласка, виберіть +, -, * або /.")
calculator()
