# shopping list array
items = []

print("Welcome to the Shopping List!")

while True:
    print("\n--- MENU ---")
    print("1. Add item")
    print("2. View list")
    print("3. Update quantity")
    print('4. Mark as purchased')
    print("5. Remove item")
    print('6. Search')
    print("7. Calculate total")
    print("8. Exit")

    choice = input("Enter your choice: ").strip()

    # 1: Add an item
    if choice == "1":
        name = input('Enter item name: ')

        if name == "":
            print("Name cannot be empty.")
        else:
            try:
                quantity = int(input("Enter quantity: "))
                price = float(input('Enter price: '))

                # create the dictionary
                new_item = {
                    "name": name,
                    'quantity': quantity,
                    "price": price,
                    'purchased': False
                }

                items.append(new_item)
                print("Item added.")
            except:
                print("Error: please enter valid numbers for quantity and price!")

    # 2: View everything
    elif choice == '2':
        if len(items) == 0:
            print("List is empty.")
        else:
            for i in range(len(items)):
                it = items[i]

                # check status
                if it["purchased"] == True:
                    status = "Purchased"
                else:
                    status = 'Pending'

                print(i + 1, "-", it['name'], "| Quantity:", it["quantity"], "| Price:", it['price'], "|", status)

    # 3: Update item count
    elif choice == "3":
        if len(items) == 0:
            print('List is empty.')
        else:
            try:
                num = int(input("Enter item number to update: "))
                if num > 0 and num <= len(items):
                    new_qty = int(input("Enter new quantity: "))
                    items[num - 1]['quantity'] = new_qty
                    print("Quantity updated.")
                else:
                    print("Bad item number.")
            except ValueError:
                print("That is not a valid number.")

    # 4: Mark as bought
    elif choice == '4':
        if not items:
            print("List is empty.")
        else:
            try:
                item_no = int(input('Enter item number: '))
                if 1 <= item_no <= len(items):
                    items[item_no - 1]["purchased"] = True
                    print("Marked as purchased.")
                else:
                    print("Invalid item number.")
            except:
                print("Please enter a valid number.")

    # 5: Delete item
    elif choice == "5":
        if len(items) == 0:
            print("List is empty.")
        else:
            try:
                idx = int(input("Enter item number to remove: "))
                if idx > 0 and idx <= len(items):
                    removed = items.pop(idx - 1)
                    print(removed['name'], "was removed.")
                else:
                    print("Bad item number.")
            except ValueError:
                print("Please enter a whole number.")

    # 6: Search
    elif choice == '6':
        word = input("Enter word to search: ").lower()
        found = False

        for x in items:
            if word in x["name"].lower():
                print("Found:", x["name"], "- Quantity:", x["quantity"])
                found = True

        if found == False:
            print("Nothing found.")

    # 7: Math / Totals
    elif choice == "7":
        total = 0
        purchased_total = 0

        for it in items:
            item_cost = it["quantity"] * it['price']
            total = total + item_cost

            if it['purchased'] == True:
                purchased_total += item_cost

        pending_total = total - purchased_total

        print("Total cost:", total)
        print('Already purchased:', purchased_total)
        print("Still need to buy:", pending_total)

    # 8: Quit
    elif choice == '8':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Pick a number from 1 to 8.")
