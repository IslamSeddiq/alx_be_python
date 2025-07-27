def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            item = input("Enter the item you want to add: ").strip().lower()
            shopping_list.append(item)
            print(f'"{item}" has been added to the list.')
        elif choice == 2:
            item = input("Enter the item you want to remove: ").strip().lower()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f'"{item}" has been removed from the list.')
            else:
                print(f'"{item}" is not found in the shopping list.')
            shopping_list.remove(item)
        elif choice == 3:
            print(shopping_list)
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Please enter a valid number.")
main()
