import csv

# File to store expenses
file_name = "expenses.csv"

def add_expense(category, amount):
    with open(file_name, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([category, amount])

def view_expenses():
    total = 0
    categories = {}
    try:
        with open(file_name, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                category, amount = row
                amount = float(amount)
                total += amount
                categories[category] = categories.get(category, 0) + amount
    except FileNotFoundError:
        print("No expenses found.")
        return

    print(f"\nTotal Spending: {total}")
    print("Category-wise Spending:")
    for category, amount in categories.items():
        print(f"{category}: {amount}")

def main():
    print("Welcome to the Personal Expense Tracker")
    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            category = input("Enter category: ")
            amount = input("Enter amount: ")
            add_expense(category, amount)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
