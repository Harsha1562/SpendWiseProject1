class Expense:
    def __init__(self, expense_id, date, category, amount, tags):
        self.expense_id = expense_id
        self.date = date
        self.category = category
        self.amount = amount
        self.tags = tags

    def to_dict(self):
        return {
            "expense_id": self.expense_id,
            "date": self.date,
            "category": self.category,
            "amount": self.amount,
            "tags": list(self.tags)
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["expense_id"],
            data["date"],
            data["category"],
            data["amount"],
            set(data["tags"])
        )

    def __str__(self):
        return f"[{self.date}] {self.category}: ${self.amount:.2f}"


class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.budget_limit = 0

    def add_expense(self, expense):
        self.expenses.append(expense)

    def get_total_spending(self):
        total = 0

        for expense in self.expenses:
            total = total + expense.amount

        return total

    def is_over_budget(self):
        return self.get_total_spending() > self.budget_limit

    def category_summary(self):
        summary = {}

        for expense in self.expenses:
            category = expense.category

            if category in summary:
                summary[category] = summary[category] + expense.amount
            else:
                summary[category] = expense.amount

        return summary

    def filter_by_category(self, category):
        result = []

        for expense in self.expenses:
            if expense.category.lower() == category.lower():
                result.append(expense)

        return result
