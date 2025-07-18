while True:
    # Prompt for a single task
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Match-case for priority
    match priority:
        case "high":
            reminder = f"Reminder: '{task}' is a high priority task."
        case "medium":
            reminder = f"Reminder: '{task}' is a medium priority task."
        case "low":
            reminder = f"Reminder: '{task}' is a low priority task."
        case _:
            reminder = f"Reminder: '{task}' has an unknown priority."

    # Time-bound logic
    if time_bound == "yes":
        reminder += " This task requires immediate attention today!"

    # Display final reminder
    print(reminder)

    # Ask if the user wants to add another task
    again = input("Do you want to enter another task? (yes/no): ").lower()
    if again != "yes":
        print("Goodbye! Stay productive.")
        break
