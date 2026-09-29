def get_number(prompt, number_type, minimum):
    """Ask until a valid number at least the minimum is entered."""
    try:
        value = number_type(input(prompt))
        if value < minimum:
            print("Please enter a number of at least", minimum)
            return None
        return value
    except ValueError:
        print("Please enter a valid number.")
        return None


def get_item_number(items, prompt):
    """Get a valid one-based item number, or return None for an empty list."""
    if len(items) == 0:
        print("List is empty.")
        return None

    try:
        number = int(input(prompt))
        if number < 1 or number > len(items):
            print("Invalid item number.")
            return None
        return number
    except ValueError:
        print("Please enter a whole number.")
        return None


def get_new_item_details():
    """Ask for a non-empty name, quantity, and price."""
    name = input("Enter item name: ").strip()
    if name == "":
        print("Name cannot be empty.")
        return None

    quantity = get_number("Enter quantity: ", int, 1)
    if quantity is None:
        return None

    price = get_number("Enter price: ", float, 0)
    if price is None:
        return None

    return name, quantity, price
