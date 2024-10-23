# Input a list of numbers
numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]

# Find minimum and maximum
minimum = min(numbers)
maximum = max(numbers)

print("Minimum value:", minimum)
print("Maximum value:", maximum)
