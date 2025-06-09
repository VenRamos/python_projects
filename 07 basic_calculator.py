"""Basic calculator with 4 functions
    add, subtract, multiply, divide
"""


def main():
    while True:
        first_num = input("First number: ")
        operator = input()
        second_num = input("Second number: ")
        op = ["+", "-", "*", "/"]
        try:
            float(first_num)
            float(second_num)
        except ValueError:
            print("Invalid Input: Digits only")
            continue
        if operator not in op:
            print("Invalid operator: Must be +, -, *, / only.")
            continue

        print(operation(first_num, operator, second_num))
        break


def operation(first_num, operator, second_num):
    if operator == "+":
        return (add(first_num, second_num))
    if operator == "-":
        return (subtract(first_num, second_num))
    if operator == "*":
        return (multiply(first_num, second_num))
    if operator == "/":
        try:
            return (divide(first_num, second_num))
        except ZeroDivisionError:
            return "Invalid input: Cannot divide by zero"


def add(first_num, second_num):
    num1 = float(first_num)
    num2 = float(second_num)
    return num1 + num2


def subtract(first_num, second_num):
    num1 = float(first_num)
    num2 = float(second_num)
    return num1 - num2


def multiply(first_num, second_num):
    num1 = float(first_num)
    num2 = float(second_num)
    return num1 * num2


def divide(first_num, second_num):
    num1 = float(first_num)
    num2 = float(second_num)
    return num1 / num2


main()
