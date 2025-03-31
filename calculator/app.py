num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
operator = input("Enter operator (+,-,*,/): ")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Invalid Input")