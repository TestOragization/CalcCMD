from Calc import Calculator

calc = Calculator()

while True:
    print("\n---Калькулятор (CMD)---")
    print("1. Математ. выражение")
    print("2. Показать историю")
    print("3. Показать историю логов пользователя")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        expression = input("Enter expression: ")
        result = calc.calculate(expression)
        print(f"Result: {result}")
    elif choice == "2":
        calc.show_history()
    elif choice == "3":
        calc.show_user_logs()
    elif choice == "4":
        calc.close()
        break
    else:
        print("Error")