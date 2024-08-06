# Check whether a string is palindrome or not
str = input("Enter a string : ")
rev = str[::-1]
if str == rev:
    print(str, " is Palindrome")
else:
    print(str," is not Palindrome")
