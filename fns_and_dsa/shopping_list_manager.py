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
        match choice:
            case 1:
                item = input("Enter the item you want to add: ").strip().lower()
                shopping_list.append(item)
                print(f'"{item}" has been added to the list.')
            case 2:
                item = input("Enter the item you want to remove: ").strip().lower()
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f'"{item}" has been removed from the list.')
                else:
                    print(f'"{item}" is not found in the shopping list.')
                shopping_list.remove(item)
            case 3:
                print(shopping_list)
            case 4:
                print("Goodbye!")
                break
            case _:
                print("Invalid option. Invalid choice. Please try again.")
