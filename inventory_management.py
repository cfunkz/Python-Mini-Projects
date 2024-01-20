items = {}


def add_item(name, barcode, quantity):
    # IF item name not in items, or barcode not in item values
    if name not in items and barcode not in {item["barcode"] for item in items.values()}:
        items[name] = {
            "barcode": barcode,
            "quantity": int(quantity)
        }
        print("Item added successfully.")
    else:
        print("Item exists. Try updating or removing.")


def update_item(input_value, quantity):
    for name, barcode in items.items():
        if input_value in [name, barcode["barcode"]]:
            items[name]["quantity"] += int(quantity)
            print(f"Quantity updated successfully. Current stock for {name}: {items[name]['quantity']}")
            break
    else:
        print("Item not found in inventory.")


def remove_item(input_value, quantity):
    for name, barcode in items.items():
        if input_value in [name, barcode["barcode"]]:
            items[name]["quantity"] -= int(quantity)
            print(f"Quantity updated successfully. Current stock for {name}: {items[name]['quantity']}")
            break
    else:
        print("Item not found in inventory.")


def find_item(input_value):
    found = False
    for name, barcode in items.items():
        if input_value in [name, barcode["barcode"]]:
            print(f"Item found: {name} | {barcode}")
        else:
            print(f"Item not found in inventory.")


def main():
    while True:
        print("""
              1. Add Item
              2. Update
              3. Remove Item
              4. Find Item
              5. Exit
              """)

        choice = input("Type an option from above: ")

        if choice not in ["1", "2", "3", "4", "5"]:
            print("Error: Invalid choice.")
        else:
            choice = int(choice)
            if choice == 1:
                name = input("Name: ")
                barcode = input("Barcode: ")
                quantity = input("Quantity: ")
                add_item(name, barcode, quantity)
            elif choice == 2:
                input_value = input("Enter name or barcode: ")
                quantity = input("Quantity: ")
                update_item(input_value, quantity)
            elif choice == 3:
                input_value = input("Enter name or barcode: ")
                amount = int(input("Amount to remove: "))
                remove_item(input_value, amount)
            elif choice == 4:
                input_value = input("Enter name or barcode: ")
                find_item(input_value)
            else:
                break


main()
