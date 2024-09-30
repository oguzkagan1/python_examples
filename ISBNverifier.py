"""The ISBN-10 verification process is used to validate book identification numbers. 
These normally contain dashes and look like: 3-598-21508-8
ISBN
The ISBN-10 format is 9 digits (0 to 9) plus one check character (either a digit or an X only). 
In the case the check character is an X, this represents the value '10'. 
These may be communicated with or without hyphens, and can be checked for their validity by the following formula:"""

def is_valid(isbn):
    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False
    total = 0
    for i in range(9):
        if not isbn[i].isdigit():
            return False
        total += int(isbn[i]) * (10 - i)
    if isbn[9] == 'X':
        total += 10 * 1 
    elif isbn[9].isdigit():
        total += int(isbn[9]) * 1  
    else:
        return False
    return total % 11 == 0

isbn_input = input("Please enter the ISBN-10 number you want to validate (e.g., 3-598-21508-8): ")

# Check the result
if is_valid(isbn_input):
    print(f"{isbn_input} is a valid ISBN-10 number.")
else:
    print(f"{isbn_input} is an invalid ISBN-10 number.")