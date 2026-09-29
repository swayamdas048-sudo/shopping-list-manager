# The shopping list is stored in this list while the program runs
items = []

print("Welcome to the Shopping List!")


while True:
    print("\nMENU")
    print("1. Add item")
    print("2. View list")
    print("3. Update quantity")
    print("4. Mark as purchased")
    print("5. Remove item")
    print("6. Search")
    print("7. Calculate total")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter item name: ")

        if name == "":
            print("Name cannot be empty.")
        else:
            try:
                quantity = int(input("Enter quantity: "))
                price = float(input("Enter price: "))

                item = {
                    "name": name,
                    "quantity": quantity,
                    "price": price,
                    "purchased": False
                }

                items.append(item)
                print("Item added.")

            except ValueError:
                print("Please enter a valid number for quantity and price.")

    elif choice == "2":
        if len(items) == 0:
            print("List is empty.")
        else:
            for i in range(len(items)):
                item = items[i]

                if item["purchased"]:
                    status = "Purchased"
                else:
                    status = "Pending"

                print(
                    i + 1, "-", item["name"],
                    "| Quantity:", item["quantity"],
                    "| Price:", item["price"],
                    "|", status
                )

    elif choice == "3":
        if len(items) == 0:
            print("List is empty.")
        else:
            try:
                number = int(input("Enter item number to update: "))

                if number > 0 and number <= len(items):
                    new_quantity = int(input("Enter new quantity: "))
                    items[number - 1]["quantity"] = new_quantity
                    print("Quantity updated.")
                else:
                    print("Bad item number.")

            except ValueError:
                print("Please enter a whole number.")

    elif choice == "4":
        if len(items) == 0:
            print("List is empty.")
        else:
            try:
                number = int(input("Enter item number: "))

                if number > 0 and number <= len(items):
                    items[number - 1]["purchased"] = True
                    print("Marked as purchased.")
                else:
                    print("Bad item number.")

            except ValueError:
                print("Please enter a whole number.")

    elif choice == "5":
        if len(items) == 0:
            print("List is empty.")
        else:
            try:
                number = int(input("Enter item number to remove: "))

                if number > 0 and number <= len(items):
                    removed_item = items.pop(number - 1)
                    print(removed_item["name"], "was removed.")
                else:
                    print("Bad item number.")

            except ValueError:
                print("Please enter a whole number.")

    elif choice == "6":
        word = input("Enter word to search: ").lower()
        found = False

        for item in items:
            if word in item["name"].lower():
                print("Found:", item["name"], "- Quantity:", item["quantity"])
                found = True

        if found == False:
            print("Nothing found.")

    elif choice == "7":
        total = 0
        purchased_total = 0

        for item in items:
            cost = item["quantity"] * item["price"]
            total = total + cost

            if item["purchased"]:
                purchased_total = purchased_total + cost

        pending_total = total - purchased_total

        print("Total cost:", total)
        print("Already purchased:", purchased_total)
        print("Still need to buy:", pending_total)

    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Pick a number from 1 to 8.")
