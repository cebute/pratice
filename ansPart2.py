def borrow(resource, quantity):
    if quantity <= 0:
        return "invalide quantity"

    if  quantity > resource["available"]:
        return "Not enough stock"

    resource["available"] -= quantity

    return "Success"

resource = {
    "name": "Laptop",
    "available": 5
}

print(borrow(resource, 2))
print(resource)

resource = {
    "name": "Laptop",
    "available": 5
}

print(borrow(resource, 8))
print(resource)