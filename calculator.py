''' This is a program that simulates basic calculator processes'''
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


print("Enter A for Addition")
print("Enter B for Subtraction")
print("Enter C for Multiplication")
print("Enter D for Division")

calculation = input("Enter the Operation required(A,B,C,D): ")

if calculation.upper() == "A":
    print(num1 + num2)
elif calculation.upper() == "B":
    print(num1 - num2)
elif calculation.upper() == "C":
    print(num1 * num2)
elif calculation.upper() == "D":
    try:
        print(num1 / num2)
    except ZeroDivisionError:
        print("Cannot divide by zero.") 
else:
    print("Enter a valid calculation")