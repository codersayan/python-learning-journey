# Input a string
string = input("Enter a string: ")

# Count vowels
vowels = "aeiouAEIOU"
count = sum(1 for char in string if char in vowels)

print("Number of vowels in the string:", count)
