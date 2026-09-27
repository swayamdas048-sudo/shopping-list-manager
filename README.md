# shopping list manager

Shopping List Manager Using Python

A Python-based shopping list management application developed as a project for Introduction to Problem Solving and Programming.

Student Information

- Name: Swayam Shree Das
- Registration No.: 26BCE11238
- Program: B.Tech CSE Core
- Semester: 1st Semester
- Course: Introduction to Problem Solving and Programming
- Faculty: Jitendra Pratap Singh Mathur

GitHub Repository

https://github.com/swayamdas048-sudo/shopping-list-manager

---

1. Project Overview

The Shopping List Manager is a Python application that helps users create and manage a personal shopping list.

Users can add items, specify quantities and prices, view their shopping list, update quantities, mark items as purchased, remove items, search for items, and calculate the estimated total cost.

The project demonstrates fundamental Python programming and problem-solving concepts through a practical real-world application.

---

2. Objectives

- Develop a practical application using Python.
- Apply fundamental programming and problem-solving concepts.
- Manage shopping items using Python data structures.
- Implement input validation and exception handling.
- Store and retrieve shopping-list data using JSON.
- Provide a simple command-line interface.
- Provide an optional browser-based interface for personal use.

---

3. Features

Shopping List Management

- Add new shopping items.
- View all items.
- Update item quantities.
- Mark items as purchased.
- Remove items.
- Search for items by name.

Cost Management

- Store the price of each item.
- Calculate the estimated total cost.
- Display purchased and pending values.

Data Persistence

Shopping-list information is stored locally in a JSON file so that the data can be loaded again when the application is restarted.

Input Validation

The application checks for:

- Empty item names.
- Invalid quantities.
- Invalid prices.
- Invalid menu selections.
- Invalid item numbers.

---

4. Python Concepts Used

The project demonstrates:

- Variables and data types
- Strings
- Lists
- Dictionaries
- Functions
- Conditional statements
- "for" loops
- "while" loops
- User input
- Input validation
- Exception handling
- File handling
- JSON
- Modules
- "pathlib"
- Program decomposition
- Command-line execution

---

5. Technologies Used

- Programming Language: Python 3
- Data Storage: JSON
- Interface: Command Line
- Optional Web Interface: Flask
- Version Control: Git and GitHub

The command-line version uses Python's standard library.

---

6. Project Structure

shopping-list-manager/
│
├── shopping_list.py
├── app.py
│
├── templates/
│   └── index.html
│
├── README.md
├── PROJECT_REPORT.md
├── requirements.txt
└── .gitignore

File Description

File| Purpose
"shopping_list.py"| Main command-line application
"app.py"| Optional Flask web application
"templates/index.html"| Web interface
"README.md"| Project documentation
"PROJECT_REPORT.md"| Project report
"requirements.txt"| Python dependencies
".gitignore"| Files excluded from Git

---

7. Requirements

Command-Line Version

- Python 3.9 or later
- Windows, Linux, or macOS
- Terminal or Command Prompt

No third-party packages are required for the command-line version.

Web Version

- Python 3.9 or later
- Flask

---

8. Installation

Clone the repository:

git clone https://github.com/swayamdas048-sudo/shopping-list-manager.git

Enter the project directory:

cd shopping-list-manager

---

9. Running the Command-Line Version

Run:

python shopping_list.py

On Windows, you can also use:

py shopping_list.py

The application displays a menu:

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

Enter the number corresponding to the required operation.

---

10. Running the Web Version

The web interface is an optional extension for personal use.

Create a virtual environment:

python -m venv .venv

Windows

.venv\Scripts\activate

Linux/macOS

source .venv/bin/activate

Install Flask:

pip install Flask

Start the application:

python app.py

Open the address displayed in the terminal, normally:

http://127.0.0.1:5000

---

11. Data Storage

Shopping-list information is stored locally in:

shopping_data.json

The file is generated automatically when data is saved.

Each item contains information such as:

{
    "name": "Milk",
    "quantity": 2,
    "price": 40,
    "purchased": false
}

---

12. Example

A user can add:

Item: Milk
Quantity: 2
Price: ₹40

The estimated cost is:

₹80

The item can then be marked as purchased or removed.

---

13. Testing

The following test cases should be performed before final submission:

Test Case| Expected Result
Add a valid item| Item is added
View shopping list| Items are displayed
Update quantity| Quantity changes
Mark item as purchased| Status changes
Search for an existing item| Matching item is displayed
Search for an unavailable item| No match is reported
Remove an item| Item is deleted
Calculate total| Estimated amount is displayed
Save and restart| Saved data is loaded
Enter invalid input| Validation message is displayed

---

14. Limitations

- The application stores data locally.
- The command-line version does not require an internet connection.
- Prices are entered manually by the user.
- There is no online product database.
- The web interface is intended for local personal use unless separately deployed.

---

15. Future Enhancements

Possible future improvements include:

- Shopping categories
- Budget limits and alerts
- Multiple shopping lists
- CSV export
- Database storage
- User accounts
- Cloud synchronization
- Product images
- Receipt generation
- Graphical user interface
- Mobile application

---

16. Course Relevance

This project is relevant to Introduction to Problem Solving and Programming because it applies fundamental programming concepts to a practical problem.

The application demonstrates problem decomposition, algorithmic thinking, variables, data structures, functions, conditional statements, loops, input validation, exception handling, file handling, and structured program organization.

---

17. Conclusion

The Shopping List Manager provides a simple way to organize shopping items and estimate expenses while demonstrating fundamental Python programming concepts.

The project combines practical problem solving with structured programming and local data storage. It can be extended with additional features such as databases, user accounts, cloud synchronization, and graphical interfaces.

---

Author

Swayam Shree Das
B.Tech CSE Core
Registration No.: 26BCE11238