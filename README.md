**#SpendWise Expense Tracker#**

SpendWise is a simple Python-based expense tracking application that helps users helps track their daily income and expenses, organize spendings into categories, set simple budget limits, and save
records to a JSON file.

**Three logical modules:**
1.models.py
2.storage.py
3.main.py

**Project Structure:**

SpendWise/
│
├── main.py
├── models.py
├── storage.py
├── utils.py
├── expenses.json
└── README.md


**File**	            **Description**

main.py	          Main application and user menu
models.py	        Contains Expense and ExpenseTracker classes
storage.py	      Saves and loads expenses using JSON
utils.py	        Date validation, ID creation, and tag processing
expenses.json     Stores expense data
README.md	        Project documentation

**Requirements:**
Python 3.14.2, The project uses only Python's built-in modules, so no external packages are required.

**How It Works:**

Run the application python main.py

Enter your budget: 800

========== SpendWise ==========
1. Add Expense
2. View Expenses
3. Category Summary
4. Search Category
5. Save and Exit
Enter your choice: 1

----- Add Expense -----
Enter date (YYYY-MM-DD): 2026-09-28
Enter category: food
Enter amount: 260
Enter tags (comma separated): breakfast,lunch
Expense added!

========== SpendWise ==========
1. Add Expense
2. View Expenses
3. Category Summary
4. Search Category
5. Save and Exit
Enter your choice: 2

----- All Expenses -----
[2026-09-28] food: $260.00

Total spending: 260.0

========== SpendWise ==========
1. Add Expense
2. View Expenses
3. Category Summary
4. Search Category
5. Save and Exit
Enter your choice: 3

----- Category Summary -----
food : $ 260.0

========== SpendWise ==========
1. Add Expense
2. View Expenses
3. Category Summary
4. Search Category
5. Save and Exit

**Technologies Used:**  Python,JSON,Regular Expressions,Object-Oriented Programming
