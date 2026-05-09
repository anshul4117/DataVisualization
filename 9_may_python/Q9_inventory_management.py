# Q9. Dictionary-based inventory management system with add, update,
#     search, and display low-stock items functionality.

def display_inventory_menu():
    """Display the inventory management menu."""
    print("\n" + "=" * 45)
    print("   INVENTORY MANAGEMENT SYSTEM")
    print("=" * 45)
    print("  1. Add Product")
    print("  2. Update Quantity")
    print("  3. Search Product")
    print("  4. Display All Products")
    print("  5. Display Low-Stock Items")
    print("  6. Remove Product")
    print("  7. Exit")
    print("=" * 45)


def add_product(inventory):
    """Add a new product to the inventory."""
    product_name = input("  Enter Product Name: ").strip().lower()
    if product_name in inventory:
        print(f"  '{product_name}' already exists. Use 'Update Quantity' instead.")
        return

    try:
        quantity = int(input("  Enter Quantity: "))
        price = float(input("  Enter Price per unit: Rs. "))
        # Store product details as a dictionary value
        inventory[product_name] = {"quantity": quantity, "price": price}
        print(f"  Product '{product_name}' added successfully!")
    except ValueError:
        print("  Invalid input. Please enter valid numbers.")


def update_quantity(inventory):
    """Update the quantity of an existing product."""
    product_name = input("  Enter Product Name to update: ").strip().lower()
    if product_name not in inventory:
        print(f"  Product '{product_name}' not found in inventory.")
        return

    try:
        new_quantity = int(input("  Enter new quantity: "))
        inventory[product_name]["quantity"] = new_quantity
        print(f"  Quantity of '{product_name}' updated to {new_quantity}.")
    except ValueError:
        print("  Invalid input. Please enter a valid integer.")


def search_product(inventory):
    """Search for a product in the inventory."""
    product_name = input("  Enter Product Name to search: ").strip().lower()
    if product_name in inventory:
        details = inventory[product_name]
        print(f"\n  --- Product Found ---")
        print(f"  Name     : {product_name.title()}")
        print(f"  Quantity : {details['quantity']}")
        print(f"  Price    : Rs. {details['price']:.2f}")
        print(f"  Value    : Rs. {details['quantity'] * details['price']:.2f}")
    else:
        print(f"  Product '{product_name}' not found in inventory.")


def display_all_products(inventory):
    """Display all products in the inventory."""
    if not inventory:
        print("\n  Inventory is empty.")
        return

    print(f"\n  {'Product':<20} {'Qty':>6} {'Price':>10} {'Value':>12}")
    print("  " + "-" * 50)
    for name, details in inventory.items():
        value = details['quantity'] * details['price']
        print(f"  {name.title():<20} {details['quantity']:>6} Rs.{details['price']:>7.2f} Rs.{value:>9.2f}")


def display_low_stock(inventory, threshold=10):
    """Display items with stock below the threshold."""
    print(f"\n  --- Low-Stock Items (Quantity < {threshold}) ---")
    low_stock_found = False

    for name, details in inventory.items():
        if details['quantity'] < threshold:
            print(f"  {name.title():<20} Qty: {details['quantity']}")
            low_stock_found = True

    if not low_stock_found:
        print("  No low-stock items found.")


def remove_product(inventory):
    """Remove a product from the inventory."""
    product_name = input("  Enter Product Name to remove: ").strip().lower()
    if product_name in inventory:
        del inventory[product_name]
        print(f"  Product '{product_name}' removed successfully!")
    else:
        print(f"  Product '{product_name}' not found in inventory.")


# --- Main Program ---
print("\n" + "=" * 45)
print("   WELCOME TO INVENTORY MANAGER")
print("=" * 45)

# Initialize inventory dictionary
product_inventory = {}

# Menu-driven loop
while True:
    display_inventory_menu()
    user_choice = input("  Enter your choice (1-7): ")

    if user_choice == '1':
        add_product(product_inventory)
    elif user_choice == '2':
        update_quantity(product_inventory)
    elif user_choice == '3':
        search_product(product_inventory)
    elif user_choice == '4':
        display_all_products(product_inventory)
    elif user_choice == '5':
        display_low_stock(product_inventory)
    elif user_choice == '6':
        remove_product(product_inventory)
    elif user_choice == '7':
        print("\n  Exiting Inventory Manager. Goodbye!")
        break
    else:
        print("  Invalid choice! Please select 1-7.")

# --- Expected Output ---
# =============================================
#    WELCOME TO INVENTORY MANAGER
# =============================================
#
# =============================================
#    INVENTORY MANAGEMENT SYSTEM
# =============================================
#   1. Add Product
#   2. Update Quantity
#   3. Search Product
#   4. Display All Products
#   5. Display Low-Stock Items
#   6. Remove Product
#   7. Exit
# =============================================
#   Enter your choice (1-7): 1
#   Enter Product Name: Laptop
#   Enter Quantity: 25
#   Enter Price per unit: Rs. 55000
#   Product 'laptop' added successfully!
#
#   Enter your choice (1-7): 1
#   Enter Product Name: Mouse
#   Enter Quantity: 5
#   Enter Price per unit: Rs. 500
#   Product 'mouse' added successfully!
#
#   Enter your choice (1-7): 4
#   Product              Qty      Price        Value
#   --------------------------------------------------
#   Laptop                25 Rs.55000.00 Rs.1375000.00
#   Mouse                  5 Rs.  500.00 Rs.  2500.00
#
#   Enter your choice (1-7): 5
#   --- Low-Stock Items (Quantity < 10) ---
#   Mouse                Qty: 5
#
#   Enter your choice (1-7): 7
#   Exiting Inventory Manager. Goodbye!
