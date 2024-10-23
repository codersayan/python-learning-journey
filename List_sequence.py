# Input a number
n = int(input("Enter a number: "))

# Generate list of squares
squares = [i ** 2 for i in range(1, n + 1)]
print("List of squares from 1 to", n, ":", squares)
