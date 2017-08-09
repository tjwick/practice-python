#!/usr/bin/env python3


string = input("Please enter a string: ")
count = len(string) - 1
isPalindrome = True

for c in string:
    if c != string[count]:
        isPalindrome = False
    count -= 1

if isPalindrome:
    print(string, "is a palindrome!")
else:
    print(string, "is not a palindrome...")
    
