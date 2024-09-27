"""Calculate the points scored in a single toss of a Darts game.
In our particular instance of the game
the target rewards 4 different amounts of points
depending on where the dart lands."""

import random
import math #Calls the math module for square root


def score(x, y):
    distance_from_center = math.sqrt(x**2 + y**2)
    if distance_from_center > 10:
        return 0  # Outside The Target
    elif distance_from_center > 5:
        return 1  # Outer circle of the targer
    elif distance_from_center > 1:
        return 5  # Dart Lands in the middle circle of the target
    else:
        return 10  # dart lands in the inner circle of the target

x, y = random.randint(0, 10), random.randint(0, 10)
print(x, y)
print(f"score of dart earn: {score(x, y)}")
