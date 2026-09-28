from models import Expense
from models import ExpenseTracker

from storage import save_expenses
from storage import load_expenses

from utils import check_date
from utils import create_id
from utils import make_tags


FILE_NAME = "expenses.json"
tracker = ExpenseTracker()
tracker.expenses = load_expenses(FILE_NAME)
try:
    tracker.budget_limit = float(input("Enter your budget: "))

except ValueError:
    print("Invalid budget.")
    tracker.budget_limit = 0

while True:

    print()
    print("========== SpendWise ==========")
    print("1. Add Expense")
    
    print("2. View Expenses")
    print("3. Category Summary")
    print("4. Search Category")
    print("5. Save and Exit")
    choice = input("Enter your choice: ")
    match choice:

        case "1":

            print()
            print("----- Add Expense -----")

            date = input("Enter date (YYYY-MM-DD): ")

            if check_date(date) == False:
                print("Invalid date!")
                continue


            category = input("Enter category: ")

            try:
                amount = float(input("Enter amount: "))

            except ValueError:
                print("Please enter a number.")
                continue

            tag_text = input("Enter tags (comma separated): ")

            tags = make_tags(tag_text)
            number = len(tracker.expenses) + 1

            expense_id = create_id(number)
            expense = Expense(
                expense_id,
                date,
                category,
                amount,
                tags
            )
            tracker.add_expense(expense)

            print("Expense added!")
        case "2":

            print()
            print("----- All Expenses -----")

            if len(tracker.expenses) == 0:

                print("No expenses found.")

            else:

                for expense in tracker.expenses:

                    print(expense)

                print()
                print(
                    "Total spending:",
                    tracker.get_total_spending()
                )
        case "3":

            print()
            print("----- Category Summary -----")

            summary = tracker.category_summary()

            for category in summary:

                print(
                    category,
                    ": $",
                    summary[category]
                )

        case "4":

            print()
            print("----- Search Category -----")

            category = input("Enter category: ")

            results = tracker.filter_by_category(category)


            if len(results) == 0:

                print("No expenses found.")

            else:

                for expense in results:

                    print(expense)

        case "5":

            save_expenses(
                FILE_NAME,
                tracker.expenses
            )

            print("Expenses saved.")
            print("Goodbye!")

            break

        case _:

            print("Invalid choice.")
