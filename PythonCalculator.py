#Python Calculator

num1 = float(input("Enter the 1st number: "))
operator = input("Enter an operator (+ - * /): ")
num2= float(input("Enter the 2sn number: "))


if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    result = num1 / num2

else:
    print(f"{operator} is not valid.")
    result = None

print(result)