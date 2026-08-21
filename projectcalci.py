# mini project to build a calculator

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
operator = input("Mention the operation to be perfromed (+, -, *, %, ** ): ")
if operator == '+':
    print(a + b)
elif operator == '-':
    print(a - b)
elif operator == '*':
    print(a * b)
elif operator == '%':
    print(a % b)
elif operator == '**':
    print(a ** b)
else:
    print("Invalid operator!")

print(" I love mathematics")
