shopping_list = []
while True:
    options = input("Choose an option(add an item, remove an item or view the list): ").strip().lower()
    match options:
        case "add an item":
            item = input("Enter the item you want to add: ").strip().lower()
            shopping_list.append(item)
            print(f'"{item}" has been added to the list.')
        case "remove an item":
            item = input("Enter the item you want to remove: ").strip().lower()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f'"{item}" has been removed from the list.')
            else:
                print(f'"{item}" is not found in the shopping list.')
            shopping_list.remove(item)
        case "view the list":
            print(shopping_list)
        case _:
            print("Invalid option. Please choose: add an item, remove an item, or view the list.")

    again = input("Do you want to do another action? (yes/no): ").strip().lower()
    if again != "yes":
        print("Goodbye!")
        break