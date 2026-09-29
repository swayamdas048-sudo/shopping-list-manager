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

