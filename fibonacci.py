# Input the number of terms
n_terms = int(input("Enter the number of terms: "))

# Initialize the first two Fibonacci numbers
a, b = 0, 1
count = 0

# Generate Fibonacci sequence
if n_terms <= 0:
    print("Please enter a positive integer.")
elif n_terms == 1:
    print("Fibonacci sequence up to", n_terms, "is:")
    print(a)
else:
    print("Fibonacci sequence:")
    while count < n_terms:
        print(a)
        nth = a + b
        # Update values
        a = b
        b = nth
        count += 1
