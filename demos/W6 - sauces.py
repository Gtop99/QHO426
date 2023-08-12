def populate(path):
    with open(path, "w") as f:
        while True:
            sauce = input("Enter a sauce you like[or \"stop\"]: ")
            if sauce.lower() == "stop":
                break
            f.write(sauce + "\n")

#populate("sauces/Konrar.txt")


def reading(path):
     with open(path) as f:
         print(f.read())


reading("sauces/Konrar.txt")
print("x" * 20)

