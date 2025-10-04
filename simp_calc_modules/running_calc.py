from simp_calc_modules import results, operations


def running_calc():
    running = True
    while running:
        print("== CALCULATOR ==")
        print("Choose an operation.")
        print("1. To ADD '+' ")
        print("2. To SUBTRACT '-' ")
        print("3. To MULTIPLY 'x' ")
        print("4. To DIVIDE '/' ")
        print("5. Show RESULTS HISTORY.")
        print("6. EXIT")

        choice = input(" > ")

        if choice == "1":
            a, b = operations.ask_numbers()
            print("Result: ", operations.add(a, b))
        elif choice == "2":
            a, b = operations.ask_numbers()
            print("Result: ", operations.subtract(a, b))
        elif choice == "3":
            a, b = operations.ask_numbers()
            print("Result: ", operations.multiply(a, b))
        elif choice == "4":
            a, b = operations.ask_numbers()
            print("Result: ", operations.divide(a, b))
        elif choice == "5":
            print(results)
        elif choice == "6":
            running = False
        else:
            print("Error!!!, Invalid Choice")
