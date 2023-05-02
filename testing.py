from Decimals import Decimals
import os

os.system("cls||clear")
print("showcasing unfinished Decimals class // addition")
print("clone of standard python library decimal module")
print("float type numbers in python lose precision after 16 digits, this class has a simple solution to that issue")
print("first adds two short decimal numbers, then two long (27) decimal numbers")
print("works anywhere with any class instance, creating a variable a and b of the Decimals class and typing c = a + b is all")
print("adds decimal digits together completely")
print("look at the code for comments")
print("\npress enter to continue")
input("...")
os.system("cls||clear")


decimalone = Decimals(2.284)
decimaltwo = Decimals(7.629)

decimalthree = decimalone + decimaltwo

print("\npress enter to continue")
input("...")
os.system("cls||clear")


print("9193737.123456789101112131415161718")
print("+")
print("73331.12345678910111213141516")

decimal_x = Decimals("9193737.123456789101112131415161718") 
decimal_y = Decimals("73331.12345678910111213141516") 

decimal_z = decimal_x + decimal_y

#for comparison
from decimal import *
getcontext().prec = 34

num1 = Decimal('9193737.123456789101112131415161718')
num2 = Decimal('73331.12345678910111213141516')

result = num1 + num2

print("answer from standard python decimal module")
print(result)

print("answer from adding the numbers together as two float type numbers")

a = 9193737.123456789101112131415161718
b = 73331.12345678910111213141516

c = a + b

print(c)
