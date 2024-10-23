# print(3+6)
# print(34-23)
# print(4*9)
# print(45/7)
# print(45//7)
# print(5%3)#modulo operator
# print(5**3) # exponential operator 5*5*5 
# Simple calculator using python 

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y == 0:
        return "Error! division by zero is not applicable...."
    return x/y

def exponent(x,y):
    return x**y

def modulus(x,y):
    if y == 0:
        return "Error! division by zero is not applicable...."
    return x%y

def calculator():
    print("Select Operation:")
    print("1. ADD")
    print("2. SUBSTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION")
    print("5. EXPONENT (POWER)")
    print("6. MODULUS")

    choice = input("Enter choice (1/2/3/4/5/6):")

    if choice in ['1', '2', '3', '4', '5', '6']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1}+{num2} = {add(num1,num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1,num2)}")
            
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1,num2)}")
            
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1,num2)}")
            
        elif choice == '5':
            print(f"{num1} ** {num2} = {exponent(num1,num2)}")
            
        elif choice == '6':
            print(f"{num1} % {num2} = {modulus(num1,num2)}")

    else:
        print("Invalid choice!!")

if __name__ == "__main__":
    calculator() 


