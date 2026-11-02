import math

number = int(input("Enter a number: "))
total = 0

for digit in str(abs(number)):
    total += math.factorial(int(digit))

if number >= 0 and total == number:
    print("Strong Number")
else:
    print("Not a Strong Number")