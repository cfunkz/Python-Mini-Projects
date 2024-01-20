import uuid
import json


def load_items_from_file():
    try:
        with open('inventory.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


items = load_items_from_file()


def save_json(filename):
    with open(filename, 'w') as file:
        json.dump(items, file)


def delete_item(input_value):
    for name, details in items.items():
        if input_value in [name, details["barcode"]]:
            del items[name]
            print(f"Item deleted successfully.")
            break
    else:
        print("Item not found in inventory.")


def add_item(name, barcode, quantity):
    # IF item name not in items, or barcode not in item values
    if int(barcode) == 0:
        code = uuid.uuid4()
        barcode = str(code)[:5]
    if name not in items and barcode not in [item["barcode"] for item in items.values()]:
        items[name] = {
            "barcode": barcode,
            "quantity": int(quantity)
        }
        save_json('inventory.json')
        print(f"Item added successfully [{name} | {barcode} | {quantity}]")
    else:
        print("Item exists. Try updating or removing.")


def update_item(input_value, quantity):
    for name, details in items.items():
        if input_value in [name, details["barcode"]]:
            items[name]["quantity"] += int(quantity)
            save_json('inventory.json')
            if items[name]["quantity"] <= 0:
                del items[name]
                save_json('inventory.json')
            print(f"Quantity updated successfully. Current stock for {name}: {items[name]['quantity']}")
            break
        else:
            print("Item not found in inventory.")


def find_item(input_value):
    for name, details in items.items():
        if input_value in [name, details["barcode"]]:
            print(f"Item found: {name} | {details}")
        else:
            print(f"Item not found in inventory.")


def view_items():
    print("\nName | Barcode | Quantity")
    print("-"*25)
    for name, details in items.items():
        barcode = details["barcode"]
        quantity = details["quantity"]
        print(f"{name} | {barcode} | {quantity}")
    print("-"*25)

def main():
    while True:
        print("Current Items: ", len(items))
        print("""
            ###################
            ## 1. Add Item   ##
            ## 2. Update     ##
            ## 3. Find Item  ##
            ## 4. View Items ##
            ## 5. Exit       ##
            ###################
              """)

        choice = input("Type an option(1-5) from above: ")

        if choice not in ["1", "2", "3", "4", "5"]:
            print("Error: Invalid choice.")
        else:
            choice = int(choice)
            if choice == 1: # Add Item
                name = input("Name: ")
                barcode = input("Barcode: ")
                quantity = input("Quantity: ")
                add_item(name, barcode, quantity)
            elif choice == 2: # Update Item
                input_value = input("Enter name or barcode: ")
                quantity = input("Do you want to increment or decrease stock? Use +/-\nQuantity: ")
                update_item(input_value, quantity)
            elif choice == 3:
                input_value = input("Enter name or barcode: ")
                find_item(input_value)
            elif choice == 4:
                view_items()
            else:
                break

main()
