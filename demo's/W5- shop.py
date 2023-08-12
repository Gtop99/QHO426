def shop():
    items = {"carrot": 0.25, "bread": 1.55, "eggs": 2.99, "milk": 1.59, "juice": 3.99}
    return items

def view_all(product = {}):
    for x , y in product.items():
        print(f"{x}--------{y}")


def playing():
    d =shop()
    d["cheese"] = 5.99
    d["milk"] = 1.99
    del d["eggs"]
    prod = input("Enter new product: ")
    price = float(input("Enter it's price:"))
    d[prod] = price
    view_all(d)


def basket():
    b = []
    while True:
        product = input("Enter an item or \"stop\": ")
        if product.upper() == "STOP":
            break
        q = int(input(f"Enter quantity of {product}: "))
        for i in range(q):
            b.append(product)
    return b


def till(basket = []):
    all_items = shop()
    total = 0
    for product in basket:
        if product.lower() in all_items:
            total += all_items[product]
        else:
            print(f"No luck. The {product}is not in stock. Go to Lidl")
    return total

def run():
    print("Welcome to Vale Shop. Please look around. We are watching you.")
    view_all(shop())
    b = basket()
    while True:
        respons = input("Are you ready to pay? [y/n]: ")
        if respons.lower() == "y":
            to_pay = till(b)
            print(f"Pay {to_pay} or i'll come after you.")
            break
        else:
            b2 = basket()
            b.extend(b2)


run()

