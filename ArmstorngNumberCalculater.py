def is_armstrong_number(number):
       digits = [int(x) for x in str(number)]
       print(digits)
       total_digits = len(digits)
       print(total_digits)
       armstorn_calculate = sum([digits ** total_digits for digits in digits])
       return armstorn_calculate

number = int(input("Armstorng Number Calculate; "))
print(is_armstrong_number(number))