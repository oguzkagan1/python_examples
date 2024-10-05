#ConcessionStand

menu = {"popcorn": 1.00,
        "hot dog": 2.00,
        "giantpretzel": 2.00,
        "asst candy": 1.00,
        "soda": 1.00,
        "bottled water": 1.00}

cart = []
total = 0

print("------- MENU ---------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}:")

print("------- MENU ---------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food)is None:
        print(f"{food} Not in Menu")
    elif menu.get(food) is not None:
        cart.append(food)

print("------ YOUR ORDER ------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ") 
print("-------------------------")

print(f"Total is: ${total:.2f}")