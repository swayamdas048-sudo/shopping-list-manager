def add_item(items, name, quantity, price):
    """Add one item to the shopping list."""
    item = {
        "name": name,
        "quantity": quantity,
        "price": price,
        "purchased": False
    }
    items.append(item)
    return item


def update_quantity(items, number, quantity):
    """Change the quantity of an item. Number is one-based."""
    items[number - 1]["quantity"] = quantity


def mark_purchased(items, number):
    """Mark an item as purchased. Number is one-based."""
    items[number - 1]["purchased"] = True


def remove_item(items, number):
    """Remove and return an item. Number is one-based."""
    return items.pop(number - 1)


def search_items(items, word):
    """Return items whose names include the search word."""
    word = word.lower()
    return [item for item in items if word in item["name"].lower()]


def calculate_totals(items):
    """Return total, purchased total, and pending total."""
    total = 0
    purchased_total = 0

    for item in items:
        cost = item["quantity"] * item["price"]
        total = total + cost
        if item["purchased"]:
            purchased_total = purchased_total + cost

    pending_total = total - purchased_total
    return total, purchased_total, pending_total
