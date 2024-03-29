class ItemToPurchase:
    # Initialize an item with default values
    def __init__(self, item_name='none', item_price=0.0, item_quantity=0, item_description='none', item_category='general'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
        self.item_category = item_category

    # Print total cost of items
    def print_item_cost(self):
        total_cost = self.item_quantity * self.item_price  
        print(f"{self.item_name} ({self.item_category}) {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")

    # Print item description
    def print_item_description(self):
        print(f"{self.item_name} ({self.item_category}): {self.item_description}")

class ShoppingCart:
    # Initialize shopping cart with default values
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    # Add an item to the cart
    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    # Remove an item from the cart
    def remove_item(self, item_name):
        item_found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                item_found = True
                break
        if not item_found:
            print("Item not found in cart. Nothing has been removed.")

    # Modify an item's quantity in the cart
    def modify_item(self, item_to_purchase):
        item_found = False
        for item in self.cart_items:
            if item.item_name == item_to_purchase.item_name:
                if item_to_purchase.item_quantity > 0:
                    item.item_quantity = item_to_purchase.item_quantity
                    item_found = True
                    print(f"{item.item_name}'s quantity updated to {item_to_purchase.item_quantity}.")
                break
        if not item_found:
            print("Item not found in cart. Nothing has been modified.")

    # Print total cost of the cart
    def print_total(self):
        total_cost = sum(item.item_quantity * item.item_price for item in self.cart_items)
        if total_cost == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {sum(item.item_quantity for item in self.cart_items)}")
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total: ${total_cost:.2f}")

    # Print descriptions of all items in the cart
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()

# Function to display menu and respond to user input
def print_menu(cart):
    menu = ("\nMENU\n"
            "a - Add item to cart\n"
            "r - Remove item from cart\n"
            "c - Change item quantity\n"
            "i - Output items' descriptions\n"
            "o - Output shopping cart\n"
            "q - Quit\n")
    command = ''
    while command != 'q':
        print(menu)
        command = input("Choose an option:\n")

        if command == 'a':
            print("\nADD ITEM TO CART")
            item_name = input("Enter the item name:\n")
            item_description = input("Enter the item description:\n")
            item_category = input("Enter the item category:\n")
            # Ensure valid price input
            while True:
                try:
                    item_price = float(input("Enter the item price:\n"))
                    if item_price < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid price. Please enter a positive number.")
            # Ensure valid quantity input
            while True:
                try:
                    item_quantity = int(input("Enter the item quantity:\n"))
                    if item_quantity < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid quantity. Please enter a positive integer.")

            item_to_purchase = ItemToPurchase(item_name, item_price, item_quantity, item_description, item_category)
            cart.add_item(item_to_purchase)
            print()

        elif command == 'r':
            print("\nREMOVE ITEM FROM CART")
            item_name = input("Enter the item name to remove:\n")
            cart.remove_item(item_name)

        elif command == 'c':
            print("\nCHANGE ITEM QUANTITY")
            item_name = input("Enter the item name:\n")
            new_quantity = int(input("Enter the new quantity:\n"))
            cart.modify_item(ItemToPurchase(item_name, item_quantity=new_quantity))

        elif command == 'o':
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()

        elif command == 'i':
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        elif command not in ['a', 'r', 'c', 'i', 'o', 'q']:
            print("Invalid option.")

# Main function to start the program
def main():
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)

main()
