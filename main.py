from shopping_list import calculate_totals, mark_purchased, remove_item, search_items, update_quantity
from item_entry import add_item_from_input
from display import show_menu, view_items
from input_helpers import get_number, get_item_number


def main():
    items = []
    print("Welcome to the Shopping List!")

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_item_from_input(items)
        elif choice == "2":
            view_items(items)
        elif choice == "3":
            number = get_item_number(items, "Enter item number to update: ")
            if number is not None:
                quantity = get_number("Enter new quantity: ", int, 1)
                if quantity is not None:
                    update_quantity(items, number, quantity)
                    print("Quantity updated.")
        elif choice == "4":
            number = get_item_number(items, "Enter item number: ")
            if number is not None:
                mark_purchased(items, number)
                print("Marked as purchased.")
        elif choice == "5":
            number = get_item_number(items, "Enter item number to remove: ")
            if number is not None:
                removed = remove_item(items, number)
                print(removed["name"], "was removed.")
        elif choice == "6":
            word = input("Enter word to search: ").strip()
            results = search_items(items, word)
            if results:
                for item in results:
                    print("Found:", item["name"], "- Quantity:", item["quantity"])
            else:
                print("Nothing found.")
        elif choice == "7":
            total, purchased, pending = calculate_totals(items)
            print("Total cost:", round(total, 2))
            print("Already purchased:", round(purchased, 2))
            print("Still need to buy:", round(pending, 2))
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Pick a number from 1 to 8.")


if __name__ == "__main__":
    main()
