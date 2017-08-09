#!/usr/bin/env python3

number = int(input("Please enter a number: "))

if (number % 2) == 0:
    if (number % 4) == 0:
        print(str(number) + " is an even number and a multiple of 4!")
    else:
        print(str(number) + " is an even number")
else:
    print(str(number) + " is an odd number")
