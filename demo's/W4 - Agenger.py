def adding(lista = []):
    new_member = input("Enter name of the avenger: ")
    lista.append(new_member)
def remove(lista = []):
    rejected = input("Enter name of avenger to be removed: ")
    if rejected in lista:
        lista.remove(rejected)
# Example:
# a = ["freed", "george", "ana","harry"]
# remove(a)
# print(a)

def printing(lista = []):
    for hero in lista:
        print(f"The mighty {hero} is part of the avengers!")
# Example:
#x = ["Kelly", "jerzy", "marius"]
#printing(x)


def run():
    avengers = []
    while True:
        opt = int(input("Avengers, Assemble!\n\n1-Add an Avenger\n2-Remove an Avenger\n3-Check on the team\n4-Exit\nOption:"))
        if opt == 1:
            adding(avengers)
        elif opt == 2:
            remove(avengers)
        elif opt == 3:
            printing(avengers)
        elif opt == 4:
            break
        else:
            print("No such option. Go to Specsavers!")
run()

