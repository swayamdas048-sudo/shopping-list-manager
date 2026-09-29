def show_menu():
    print("\n--- SHOPPING LIST MENU ---")
    print("1. Add item")
    print("2. View list")
    print("3. Update quantity")
    print("4. Mark as purchased")
    print("5. Remove item")
    print("6. Search")
    print("7. Calculate total")
    print("8. Exit")


def view_items(items):
    if len(items) == 0:
        print("List is empty.")
        return

    for index in range(len(items)):
        item = items[index]
        if item["purchased"]:
            status = "Purchased"
        else:
            status = "Pending"

        print(index + 1, "-", item["name"],
              "| Quantity:", item["quantity"],
              "| Price:", item["price"], "|", status)
