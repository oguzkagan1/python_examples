
def square(number):
    if number <= 64 and number > 0:
        number = (2 ** number) / 2
    else:
        raise ValueError("square must be between 1 and 64")
    return number
    "how many grains were on a given square"

def total():
    total_grain = 0
    for n in range(1, 65):
        total_grain += int((2 ** n) / 2)
        print(total_grain)
    return total_grain
    "the total number of grains on the chessboard"

number = 16  #You can find out how many grains of wheat fall on which square.
print(square(number)) 
print(total()) #You can find out how many total grains on chessboard.
