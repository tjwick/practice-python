#!/usr/bin/env python3
import datetime

name = input("Please enter your name: ")
age = input("Please enter your age: ")
printCount = int(input("How many times should we print it: "))

while (printCount > 0):
    print(name + ", you will turn 100 years old in the year " + str(datetime.date.today().year - int(age) + 100))
    printCount -= 1
