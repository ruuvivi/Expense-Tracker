def menu_display():
    print("-----EXPENSE TRACKER-----")
    print("1. Add a new expense")
    print("2. Delete an expense")
    print("3. View all expenses")
    print("4. Filter expenses by category")
    print("5. Calculate total expenses")
    print("6. Save expenses to a file")
    print("7. Read expenses from a file")
    print("8. Exit")
    
def add_expenses(expenses):
    description = input("Enter description: ")
    category = input("Enter category: ")
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount < 0:
                print("Please give a positive number.")
                continue
            break
        except ValueError:
            print("Give a valid number.")
    expense = {"description": description, "category": category, "amount": amount}
    expenses.append(expense)
    print("Expense added!")

def view_expenses(expenses):
    if expenses:
        print(f"{'Description':<20}{'Category':<20}{'Amount':<10}")
        print("-" * 50)
        for expense in expenses:
            print(f"{expense['description']:<20}{expense['category']:<20}{expense['amount']:<10.2f}")
    else:
        print("No expenses found.")
        
def filter_expenses(expenses):
    if expenses:
        filter_category = input("Enter category to filter: ")
        found = False
        print(f"{'Description':<20}{'Category':<20}{'Amount':<10}")
        print("-" * 50)
        for expense in expenses:
            if expense["category"] == filter_category:
                print(f"{expense['description']:<20}{expense['category']:<20}{expense['amount']:<10.2f}")
                found = True
        if not found:
            print("No expenses found for the given category.")
    else:
        print("There are no expenses.")

def total_expenses(expenses):
    if not expenses:
        print("There are no expenses.")
        return
    total = sum(expense["amount"] for expense in expenses)
    print("Total expenses:", total)

def delete_expenses(expenses):
    if expenses:
        filter_description = input("Enter description of expense to delete: ")
        for expense in expenses:
            if expense["description"] == filter_description:
                expenses.remove(expense)
                print("Expense deleted!")
                return
        print("Expense not found.")
    else:
        print("There are no expenses.")

def save_expenses(expenses):
    file_name = input("Enter a desired filename: ")

    with open(file_name, 'w') as f:
        f.write(f"{'Description':<20}{'Category':<20}{'Amount':<10}\n")
        f.write("-" * 50 + "\n")
        for expense in expenses:
            f.write(f"{expense['description']:<20}{expense['category']:<20}{expense['amount']:<10.2f}\n")
        print("File written to", file_name)

    f.close()

def read_expenses(expenses):
    if expenses:
        file_name = input("Enter the filename to read from: ")
        try:
            with open(file_name, 'r') as f:
                print(f.read())
        except FileNotFoundError:
            print("File not found. Does the file exists?")
    else:
        print("There are no files.")

def main():
    expenses = []
    while True:
        menu_display()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_expenses(expenses)
            elif choice == 2:
                delete_expenses(expenses)
            elif choice == 3:
                view_expenses(expenses)
            elif choice == 4:
                filter_expenses(expenses)
            elif choice == 5:
                total_expenses(expenses)
            elif choice == 6:
                save_expenses(expenses)
            elif choice == 7:
                read_expenses(expenses)
            elif choice == 8:
                yesno = input("Are you sure you want to exit the program? yes/no: ").strip().lower()
                if yesno == "yes":
                    print("Exiting program. Goodbye!")
                    break
            else:
                print("Invalid choice. Please try again!")
        except ValueError:
            print("Please give a choice between 1-8.")

main()