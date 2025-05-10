class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_item(self, item_name, price):
        if item_name in self.cart:
            print(f"{item_name} is already in the cart.")
        else:
            self.cart[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.cart:
            del self.cart[item_name]
        else:
            print(f"{item_name} is not in the cart.")

    def calculate_total(self):
        return sum(self.cart.values())

    def display_cart(self):
        print("Current Items in Cart:")
        for item, price in self.cart.items():
            print(f"{item} - {price}")
        print(f"Total Quantity: {self.calculate_total()}")


# Example usage
cart = ShoppingCart()
cart.add_item("Papaya", 100)
cart.add_item("Guava", 200)
cart.add_item("Orange", 150)
cart.display_cart()

print("\nUpdated Items in Cart after removing Orange:")
cart.remove_item("Orange")
cart.display_cart()