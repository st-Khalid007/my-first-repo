import simp_calc_modules.results as results


def add(a, b):
    answer = a + b
    results.add_to_result(answer)
    return answer


def subtract(a, b):
    answer = a - b
    results.add_to_result(answer)
    return answer


def multiply(a, b):
    answer = a * b
    results.add_to_result(answer)
    return answer


def divide(a, b):
    answer = a / b
    results.add_to_result(answer)
    return answer


def ask_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b
