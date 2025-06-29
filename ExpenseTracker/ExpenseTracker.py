import datetime

# Global list to store expenses
expenses = []

# Function to add an expense
def add_expense():
    try:
        amount = float(input("Enter amount: ₹"))
        category = input("Enter category (e.g., Food, Travel, Bills): ")
        date_input = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
        if date_input:
            date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
        else:
            date = datetime.date.today()

        expense = {"amount": amount, "category": category, "date": date}
        expenses.append(expense)
        print("✅ Expense added successfully!")

    except ValueError:
        print("❗ Invalid input. Please try again.")

# Function to view all expenses
def view_expenses():
    if not expenses:
        print("No expenses to show.")
        return

    print("\n📋 All Expenses:")
    for idx, e in enumerate(expenses, start=1):
        print(f"{idx}. ₹{e['amount']} - {e['category']} on {e['date']}")
    print()

# Function to show monthly summary
def monthly_summary():
    if not expenses:
        print("No expenses recorded yet.")
        return

    summary = {}
    for e in expenses:
        month = e['date'].strftime("%Y-%m")
        summary[month] = summary.get(month, 0) + e['amount']

    print("\n📊 Monthly Summary:")
    for month, total in sorted(summary.items()):
        print(f"{month}: ₹{total:.2f}")
    print()

# Menu loop
def main():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Monthly Summary")
        print("0. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            monthly_summary()
        elif choice == "0":
            print("👋 Exiting... Have a great day!")
            break
        else:
            print("❗ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
