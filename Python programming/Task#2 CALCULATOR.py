# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    return x / y

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Take input from the user
choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result:", add(num1, num2))

elif choice == '2':
    print("Result:", subtract(num1, num2))

elif choice == '3':
    print("Result:", multiply(num1, num2))

elif choice == '4':
    if num2 == 0:
        print("Error! Division by zero is not allowed.")
    else:
        print("Result:", divide(num1, num2))

else:
    print("Invalid input")
