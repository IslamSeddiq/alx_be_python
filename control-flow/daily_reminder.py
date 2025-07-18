while True:
    # Get task details from user
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Use match-case to construct base message
    match priority:
        case "high":
            if time_bound == "yes":
                print(f"\nReminder: '{task}' is a high priority task that requires immediate attention today!\n")
            else:
                print(f"\nNote: '{task}' is a high priority task. Plan to complete it soon.\n")

        case "medium":
            if time_bound == "yes":
                print(f"\nReminder: '{task}' is a medium priority task that should be done today.\n")
            else:
                print(f"\nNote: '{task}' is a medium priority task. Try to complete it this week.\n")

        case "low":
            if time_bound == "yes":
                print(f"\nReminder: '{task}' is a low priority task but still needs to be done today.\n")
            else:
                print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time.\n")

        case _:
            print("\nInvalid priority entered. Please use high, medium, or low.\n")

    # Ask to continue
    again = input("Do you want to enter another task? (yes/no): ").lower()
    if again != "yes":
        print("Goodbye! Stay organized.")
        break
