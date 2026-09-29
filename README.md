# Shopping List Manager

A beginner-friendly command-line shopping list program written in Python. It lets the user add, view, update, purchase, remove, and search for items, then calculate shopping costs.

## Requirements

- Python 3.9 or newer
- No extra packages are needed

## Run

Open a terminal in this folder and run:

```text
python main.py
```

On Windows, you can also use:

```text
py main.py
```

The list is kept in memory and is cleared when the program exits.

## Project files

- `main.py` runs the menu and connects the parts of the program.
- `shopping_list.py` contains the list operations and cost calculations.
- `display.py` prints the menu and shopping list.
- `input_helpers.py` checks user input.
- `item_entry.py` groups the prompts used when adding an item.
- `tests/test_shopping_list.py` checks the main list operations.

## Run the checks

```text
python -m unittest discover -s tests -t .
```

## Project Output

When the program starts, it displays the welcome message and menu:

```text
Welcome to the Shopping List!

--- SHOPPING LIST MENU ---
1. Add item
2. View list
3. Update quantity
4. Mark as purchased
5. Remove item
6. Search
7. Calculate total
8. Exit

For example, after adding an item, viewing the list, and calculating the total, the program may display:
Item added.
1 - Milk | Quantity: 2 | Price: 40.0 | Pending
Total cost: 80.0
Already purchased: 0
Still need to buy: 80.0
The exact output depends on the items and choices entered by the user.
```

<img width="1920" height="1080" alt="Screenshot (43)" src="https://github.com/user-attachments/assets/8991ddb0-10d7-4414-8e3e-3525b9a576e0" />
<img width="1920" height="1080" alt="Screenshot (44)" src="https://github.com/user-attachments/assets/5047d8b7-00d1-4fc3-bed6-79c7c7f0ade6" />
<img width="1920" height="1080" alt="Screenshot (46)" src="https://github.com/user-attachments/assets/b483913d-b904-4cfe-8e6b-3bf32cf57d82" />
<img width="1920" height="1080" alt="Screenshot (47)" src="https://github.com/user-attachments/assets/833e1340-022a-4d42-907c-72da35a47eb5" />



