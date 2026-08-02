class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Store:
    def __init__(self):
        self.inventory = []

    def add_product(self, product_object):
        self.inventory.append(product_object)

    def total_inventory_value(self):
        total = 0

        for product in self.inventory:
            total += product.price * product.quantity

        return total


# Creating Products
p1 = Product("Laptop", 50000, 5)
p2 = Product("Mouse", 800, 10)
p3 = Product("Keyboard", 1500, 7)


store = Store()

store.add_product(p1)
store.add_product(p2)
store.add_product(p3)

print("Inventory:")
for item in store.inventory:
    print(item.name, item.price, item.quantity)

print("\nTotal Inventory Value =", store.total_inventory_value())