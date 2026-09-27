"""
Shopping List Manager
Course: Introduction to Problem Solving and Programming
Student: Swayam Shree Das

A terminal-based shopping list application using Python fundamentals.
"""

import json
from pathlib import Path

DATA_FILE = Path("shopping_data.json")


def load_items():
    """Load shopping items from the JSON file."""
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read saved data. Starting with an empty list.")
        return []


def save_items(items):
    """Save shopping items to the JSON file."""
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(items, file, indent=4)
        print("Shopping list saved.")
    except OSError as error:
        print(f"Could not save the shopping list: {error}")


def get_positive_integer(prompt):
    """Read a positive integer from the user."""
    while True:
        try:
            value = int(input(prompt).strip())
            if value > 0:
                return value
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a valid whole number.")


def get_non_negative_float(prompt):
    """Read a non-negative price from the user."""
    while True:
        try:
            value = float(input(prompt).strip())
            if value >= 0:
                return value
            print("Price cannot be negative.")
        except ValueError:
            print("Please enter a valid number.")


def add_item(items):
    """Add a new item to the shopping list."""
    name = input("Enter item name: ").strip()

    if not name:
        print("Item name cannot be empty.")
        return

    quantity = get_positive_integer("Enter quantity: ")
    price = get_non_negative_float("Enter price per item (₹): ")

    items.append({
        "name": name,
        "quantity": quantity,
        "price": price,
        "purchased": False
    })

    save_items(items)
    print(f'"{name}" was added to the shopping list.')


def view_items(items):
    """Display all shopping-list items."""
    if not items:
        print("\nYour shopping list is empty.")
        return

    print("\n" + "=" * 72)
    print(f"{'No.':<5}{'Item':<24}{'Qty':<8}{'Price':<14}{'Status':<12}")
    print("=" * 72)

    for index, item in enumerate(items, start=1):
        status = "Purchased" if item["purchased"] else "Pending"
        print(
            f"{index:<5}"
            f"{item['name'][:22]:<24}"
            f"{item['quantity']:<8}"
            f"₹{item['price']:<13.2f}"
            f"{status:<12}"
        )

    print("=" * 72)


def choose_item(items, prompt):
    """Return a zero-based item index selected by the user."""
    if not items:
        print("The shopping list is empty.")
        return None

    view_items(items)
    number = get_positive_integer(prompt)

    if number > len(items):
        print("Invalid item number.")
        return None

    return number - 1


def update_quantity(items):
    """Change the quantity of an existing item."""
    index = choose_item(items, "Enter item number to update: ")
    if index is None:
        return

    items[index]["quantity"] = get_positive_integer("Enter new quantity: ")
    save_items(items)
    print("Quantity updated.")


def mark_purchased(items):
    """Toggle the purchased status of an item."""
    index = choose_item(items, "Enter item number to mark as purchased: ")
    if index is None:
        return

    items[index]["purchased"] = True
    save_items(items)
    print(f'"{items[index]["name"]}" marked as purchased.')


def remove_item(items):
    """Remove an item from the shopping list."""
    index = choose_item(items, "Enter item number to remove: ")
    if index is None:
        return

    removed = items.pop(index)
    save_items(items)
    print(f'"{removed["name"]}" was removed.')


def search_item(items):
    """Search for items by name."""
    if not items:
        print("The shopping list is empty.")
        return

    keyword = input("Enter item name or keyword: ").strip().lower()

    matches = [
        item for item in items
        if keyword in item["name"].lower()
    ]

    if not matches:
        print("No matching items found.")
        return

    print("\nMatching items:")
    for item in matches:
        status = "Purchased" if item["purchased"] else "Pending"
        subtotal = item["quantity"] * item["price"]
        print(
            f"- {item['name']} | Quantity: {item['quantity']} | "
            f"Subtotal: ₹{subtotal:.2f} | {status}"
        )


def calculate_total(items):
    """Calculate the estimated total cost of all items."""
    if not items:
        print("The shopping list is empty.")
        return

    total = sum(item["quantity"] * item["price"] for item in items)
    purchased_total = sum(
        item["quantity"] * item["price"]
        for item in items
        if item["purchased"]
    )
    pending_total = total - purchased_total

    print(f"\nEstimated total: ₹{total:.2f}")
    print(f"Purchased value: ₹{purchased_total:.2f}")
    print(f"Pending value: ₹{pending_total:.2f}")


def display_menu():
    """Display the main menu."""
    print(
        """
========================================
       SHOPPING LIST MANAGER
========================================
1. Add item
2. View shopping list
3. Update quantity
4. Mark item as purchased
5. Remove item
6. Search item
7. Calculate estimated total
8. Save shopping list
9. Exit
========================================
"""
    )


def main():
    """Run the Shopping List Manager."""
    items = load_items()

    print("Welcome to the Shopping List Manager!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            add_item(items)
        elif choice == "2":
            view_items(items)
        elif choice == "3":
            update_quantity(items)
        elif choice == "4":
            mark_purchased(items)
        elif choice == "5":
            remove_item(items)
        elif choice == "6":
            search_item(items)
        elif choice == "7":
            calculate_total(items)
        elif choice == "8":
            save_items(items)
        elif choice == "9":
            save_items(items)
            print("Thank you for using the Shopping List Manager.")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 9.")


if __name__ == "__main__":
    main()
