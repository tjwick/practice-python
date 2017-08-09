#!/usr/bin/env python3

num = int(input("Please enter a number: "))

potentialDivisors = range(2, num - 2)
divisors = []

for i in potentialDivisors:
    if num % i == 0:
        divisors.append(i)

print(divisors)
