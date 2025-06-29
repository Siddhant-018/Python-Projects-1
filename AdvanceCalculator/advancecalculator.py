import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error: Cannot take square root of a negative number!"
    return math.sqrt(x)

def factorial(x):
    if x < 0:
        return "Error: Factorial of negative number not defined!"
    return math.factorial(int(x))

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def show_menu():
    print("\n==== Advanced Calculator ====")
    print("1. Addition (x + y)")
    print("2. Subtraction (x - y)")
    print("3. Multiplication (x * y)")
    print("4. Division (x / y)")
    print("5. Power (x ^ y)")
    print("6. Square Root (√x)")
    print("7. Factorial (x!)")
    print("8. Sine (sin x)")
    print("9. Cosine (cos x)")
    print("10. Tangent (tan x)")
    print("0. Exit")

while True:
    show_menu()
    choice = input("Enter choice (0-10): ")

    if choice == "0":
        print("Exiting... Goodbye!")
        break

    if choice in ["1", "2", "3", "4", "5"]:
        x = float(input("Enter first number (x): "))
        y = float(input("Enter second number (y): "))

        if choice == "1":
            print("Result:", add(x, y))
        elif choice == "2":
            print("Result:", subtract(x, y))
        elif choice == "3":
            print("Result:", multiply(x, y))
        elif choice == "4":
            print("Result:", divide(x, y))
        elif choice == "5":
            print("Result:", power(x, y))

    elif choice in ["6", "7", "8", "9", "10"]:
        x = float(input("Enter the number (x): "))

        if choice == "6":
            print("Result:", square_root(x))
        elif choice == "7":
            print("Result:", factorial(x))
        elif choice == "8":
            print("Result:", sin(x))
        elif choice == "9":
            print("Result:", cos(x))
        elif choice == "10":
            print("Result:", tan(x))
    else:
        print("Invalid input! Try again.")
