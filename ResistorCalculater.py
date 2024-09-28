color_codes = {
    'siyah': (0, 1),
    'kahverengi': (1, 10, 1),
    'kırmızı': (2, 100, 2),
    'turuncu': (3, 1000),
    'sarı': (4, 10000),
    'yeşil': (5, 100000, 0.5),
    'mavi': (6, 1000000, 0.25),
    'mor': (7, 10000000, 0.1),
    'gri': (8, None, 0.05),
    'beyaz': (9, None),
    'altın': (None, 0.1, 5),
    'gümüş': (None, 0.01, 10)
}

first_color = input("Enter First Band Color: ").lower()
second_color = input("Enter Second Band Color: ").lower()
third_color = input("Enter Third Band Color: ").lower()
fourth_color = input("Fourth Band Color: ").lower()

first_digit = color_codes[first_color][0]
second_digit = color_codes[second_color][0]
third_digit = color_codes[third_color][1]
fourth_digit = color_codes[fourth_color][2]

total_resist = (first_digit * 10 + second_digit) * third_digit

print(f"Total Resist: {total_resist} ohm ±{fourth_digit}")