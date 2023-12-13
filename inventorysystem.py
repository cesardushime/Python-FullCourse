# Initialize an empty inventory dictionary to store items
inventory = {}

# Function to add items to inventory
def add_item(name, price, quantity):
    if name not in inventory:
        inventory[name] = {'price': price, 'quantity': quantity}
        print(f"{name} added to inventory.")
    else:
        print(f"{name} already exists in inventory.")

# Function to remove items from inventory
def remove_item(name):
    if name in inventory:
        del inventory[name]
        print(f"{name} removed from inventory.")
    else:
        print(f"{name} does not exist in inventory.")

# Function to update item details
def update_item(name, price=None, quantity=None):
    if name in inventory:
        if price:
            inventory[name]['price'] = price
        if quantity:
            inventory[name]['quantity'] = quantity
        print(f"{name} details updated.")
    else:
        print(f"{name} does not exist in inventory.")

# Function to display inventory
def display_inventory():
    print("Current Inventory:")
    for item, details in inventory.items():
        print(f"{item} - Price: {details['price']}, Quantity: {details['quantity']}")

# Function to calculate total inventory value
def calculate_inventory_value():
    total_value = 0
    for details in inventory.values():
        total_value += details['price'] * details['quantity']
    print(f"Total Inventory Value: ${total_value}")

# User interface loop
while True:
    print("\nWhat would you like to do?")
    print("1. Add item to inventory")
    print("2. Remove item from inventory")
    print("3. Update item details")
    print("4. Display inventory")
    print("5. Calculate inventory value")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))
        add_item(name, price, quantity)
    elif choice == '2':
        name = input("Enter item name to remove: ")
        remove_item(name)
    elif choice == '3':
        name = input("Enter item name to update: ")
        price = float(input("Enter new price (leave blank to keep current): ") or 0)
        quantity = int(input("Enter new quantity (leave blank to keep current): ") or 0)
        update_item(name, price, quantity)
    elif choice == '4':
        display_inventory()
    elif choice == '5':
        calculate_inventory_value()
    elif choice == '6':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
