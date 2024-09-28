"""A perfect number is a positive integer that is equal to the sum of its proper divisors, 
excluding the number itself. In other words, if you add up all the divisors of the number (excluding the number), 
the sum will equal the original number."""


def classify(number):
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    aliquot = sum(i for i in range(1, number) if number %i == 0) #This line computes the sum of all divisors of number, excluding the number itself. 
    print(aliquot)
    if aliquot == number:
        return "perfect"
    elif aliquot > number:
        return "abundant"
    else:
        return "deficient"
    
number = int(input("Enter your number: "))
result = classify(number)
print(f"{number} is {result}")