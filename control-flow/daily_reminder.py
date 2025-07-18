while True:
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Note: '{task}' is a high priority task. Plan to complete it soon.")

        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task that should be done today.")
            else:
                print(f"Note: '{task}' is a medium priority task. Try to complete it this week.")

        case "low":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a low priority task but still needs to be done today.")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")

        case _:
            print("Invalid priority entered. Please use high, medium, or low.")

    again = input("Do you want to enter another task? (yes/no): ").lower()
    if again != "yes":
        break
