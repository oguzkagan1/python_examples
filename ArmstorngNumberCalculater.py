"""An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits."""
def is_armstrong_number(number):
       digits = [int(x) for x in str(number)]
       print(digits)
       total_digits = len(digits)
       print(total_digits)
       armstorn_calculate = sum([digit ** total_digits for digit in digits])
       return armstorn_calculate

number = int(input("Armstorng Number Calculate; "))
print(is_armstrong_number(number))