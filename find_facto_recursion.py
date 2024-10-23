# Function to calculate factorial recursively
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Input a number
num = int(input("Enter a number: "))
print("The factorial of", num, "is:", factorial(num))
