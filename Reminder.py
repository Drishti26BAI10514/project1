import datetime

FILE_NAME = "reminders.txt"


def load_reminders_from_file():
    reminders_list = []
    try:
        with open(FILE_NAME, "r") as file_handle:
            for line in file_handle:
                cleaned_line = line.strip()
                if cleaned_line:
                    fields = cleaned_line.split('|')
                    if len(fields) == 4:
                        reminder_data = {
                            "title": fields[0],
                            "date": fields[1],
                            "time": fields[2],
                            "status": fields[3]
                        }
                        reminders_list.append(reminder_data)
    except FileNotFoundError:
        # The file will be created upon saving the first reminder.
        pass
    return reminders_list


def save_reminders_to_file(reminders_data):
    with open(FILE_NAME, "w") as file_handle:
        for reminder_item in reminders_data:
            file_handle.write(
                f"{reminder_item['title']}|{reminder_item['date']}|{reminder_item['time']}|{reminder_item['status']}\n"
            )


def add_new_reminder(current_reminders):
    print("\n--- ADD REMINDER ---")
    reminder_title = input("Enter reminder title: ")

    # Date input and validation
    while True:
        reminder_date = input("Enter date (DD-MM-YYYY): ")
        try:
            datetime.datetime.strptime(reminder_date, "%d-%m-%Y")
            break
        except ValueError:
            print("Invalid date format. Please use DD-MM-YYYY.")

    # Time input and validation
    while True:
        reminder_time = input("Enter time (HH:MM): ")
        try:
            datetime.datetime.strptime(reminder_time, "%H:%M")
            break
        except ValueError:
            print("Invalid time format. Please use HH:MM.")

    new_reminder = {
        "title": reminder_title,
        "date": reminder_date,
        "time": reminder_time,
        "status": "Pending"
    }
    current_reminders.append(new_reminder)
    save_reminders_to_file(current_reminders)
    print("Reminder successfully added.")


def display_all_reminders(current_reminders):
    print("\n--- ALL REMINDERS ---")
    if not current_reminders:
        print("No reminders are currently stored.")
        return

    for index, reminder in enumerate(current_reminders):
        print(f"\nReminder No.: {index + 1}")
        print(f"Title  : {reminder['title']}")
        print(f"Date   : {reminder['date']}")
        print(f"Time   : {reminder['time']}")
        print(f"Status : {reminder['status']}")


def find_reminders_by_keyword(current_reminders):
    print("\n--- SEARCH REMINDER ---")
    search_term = input("Enter title to search: ").lower()
    found_match = False
    for index, reminder in enumerate(current_reminders):
        if search_term in reminder["title"].lower():
            print(f"\nReminder No.: {index + 1}")
            print(f"Title  : {reminder['title']}")
            print(f"Date   : {reminder['date']}")
            print(f"Time   : {reminder['time']}")
            print(f"Status : {reminder['status']}")
            found_match = True
    if not found_match:
        print("No reminders matching the search term were found.")


def mark_reminder_as_complete(current_reminders):
    display_all_reminders(current_reminders)
    if not current_reminders:
        return

    try:
        reminder_number = int(input("\nEnter the number of the reminder to mark as complete: "))
        if 1 <= reminder_number <= len(current_reminders):
            current_reminders[reminder_number - 1]["status"] = "Completed"
            save_reminders_to_file(current_reminders)
            print("Reminder has been marked as completed.")
        else:
            print("Invalid reminder number provided.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def remove_reminder(current_reminders):
    display_all_reminders(current_reminders)
    if not current_reminders:
        return

    try:
        reminder_number = int(input("\nEnter the number of the reminder to delete: "))
        if 1 <= reminder_number <= len(current_reminders):
            removed_reminder = current_reminders.pop(reminder_number - 1)
            save_reminders_to_file(current_reminders)
            print(f"Deleted reminder: {removed_reminder['title']}")
        else:
            print("Invalid reminder number provided.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def run_reminder_system():
    active_reminders = load_reminders_from_file()

    while True:
        print("\n================================")
        print("   REMINDER MANAGEMENT SYSTEM")
        print("================================")
        print("1. Add Reminder")
        print("2. View Reminders")
        print("3. Search Reminder")
        print("4. Mark Reminder as Completed")
        print("5. Delete Reminder")
        print("6. Exit")

        user_choice = input("\nEnter your selection: ")

        if user_choice == "1":
            add_new_reminder(active_reminders)
        elif user_choice == "2":
            display_all_reminders(active_reminders)
        elif user_choice == "3":
            find_reminders_by_keyword(active_reminders)
        elif user_choice == "4":
            mark_reminder_as_complete(active_reminders)
        elif user_choice == "5":
            remove_reminder(active_reminders)
        elif user_choice == "6":
            print("\nExiting Reminder Management System. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose a number between 1 and 6.")


if __name__ == "__main__":
    run_reminder_system()