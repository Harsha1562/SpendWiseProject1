import json
from models import Expense


def save_expenses(filename, expenses):

    data = []

    for expense in expenses:
        data.append(expense.to_dict())

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def load_expenses(filename):

    try:

        with open(filename, "r") as file:
            data = json.load(file)

        expenses = []

        for item in data:
            expense = Expense.from_dict(item)
            expenses.append(expense)

        return expenses

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("JSON file is empty or damaged.")
        return []

    except ValueError:
        print("Invalid data in JSON file.")
        return []
