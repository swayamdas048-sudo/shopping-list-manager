from input_helpers import get_new_item_details
from shopping_list import add_item


def add_item_from_input(items):
    details = get_new_item_details()
    if details is None:
        return

    name, quantity, price = details
    add_item(items, name, quantity, price)
    print("Item added.")
