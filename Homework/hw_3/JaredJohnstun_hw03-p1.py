#Jared Johnstun
#Date: 9/16/2024
import os

x = input("Please enter a number: ")
x = float(x)
y = input("Please enter a second number: ")
y = float(y)

print(f'Your two numbers are {x, y}')
add = x+y
subtract = x-y
multiply = x*y
divide = x/y
print(f'x + y = {add: >7.2f}')
print(f'x - y = {subtract: >7.2f}')
print(f'x * y = {multiply: >7.2f}')
print(f'x / y = {divide: >7.2f}')