#while not none work


menu = ["a", "b", "c"]

for x in menu:
    print(x, end=" ")
    while True:
        ara = input("aramak istediginiz harfi giriniz")
        if ara == "q":
            break
        elif ara in menu:
            print("var")
        else:
            print("yok")
