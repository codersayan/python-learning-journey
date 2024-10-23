# Input a string
string = input("Enter a string: ")

# Check for palindrome
if string == string[::-1]:
    print(string, "is a palindrome.")
else:
    print(string, "is not a palindrome.")
