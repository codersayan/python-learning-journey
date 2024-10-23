# Input a number
num = int(input("Enter an integer: "))

# Count digits
count = 0
while num != 0:
    num //= 10
    count += 1

print("Number of digits:", count)
