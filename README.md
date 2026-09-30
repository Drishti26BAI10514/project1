# Reminder Management System
A simple Reminder Management System with Python CLI.
This project is for practising functions, file handling, user input, validation of dates/times, lists, dictionaries and CRUD basics.
The program also dynamically stores the reminders in a local file called 'reminders.txt', so the program can load any previously saved reminders on launching.
## Features
You can Add a new reminder
View all the saved reminders
Search for a reminder by the title
Mark a reminder as done
Delete a reminder
Validate the dates/times before creating reminder
Save reminders locally by a text file
## How It Works
When adding a reminder, the program will ask
- Reminder Title
- Date (DD-MM-YYYY)
- Time (HH:MM)
A new reminder is created with status Pending.
When a reminder is marked as done, its status changes to Completed.
All the saved reminders will be loaded from 'reminders.txt' when the program is launched.
## Project Structure
```text
reminder-project/
│
├── Reminder.py
├── README.md
├── requirements.txt
└── reminders.txt
```
'reminders.txt' file is automatically created once the first reminder is saved
## Requirements
Python 3.13.3
No third-party modules
The project uses datetime from Python's standard library
## How to Run
Run the program from project folder (VS Code or terminal) by
```bash
python Reminder.py
```
If your system requires: 
```bash
python3 Reminder.py
```
## Main Menu 
```text
================================
REMINDER MANAGEMENT SYSTEM
================================
1. Add Reminder
2. View Reminders
3. Search Reminder
4. Mark Reminder as Completed
5. Delete Reminder
6. Exit
```
Type the number of the operation you want to do.
## Sample
"""text
--- ADD REMINDER ---
Enter reminder title: Submit assignment
Enter date (DD-MM-YYYY): 30-09-2026
Enter time (HH:MM): 18:30
Reminder successfully added.
"""
## Data Storage
The reminders are stored in a plain text file, named `reminders.txt`.
Each reminder is stored in one line using `|` to separate the fields.
Example:
```text
Submit assignment|30-09-2026|18:30|Pending
```
The four fields are:
1. Title
2. Date
3. Time
4. Status
## Python Concepts Used
- Functions
- Lists
- Dictionaries
- Strings
- `if/elif/else`
- `while` loops
- `for` loops
- User input
- Exception handling
- File handling
- Reading/writing text files
- Date and time validation
- Searching
- Updating
- Deleting
## Limitations
This is a super-basic local command-line app, and it doesn't bark at you with:
- Graphical interface
- Notification/Alarms
- Database
- Account
- Cloud-sync
- Scheduler
- Auto-sorting by date
The text-file approach keeps the project simple for learning purposes.
## Future Enhancements
Some possible enhancements could be:
- Add a GUI with Tkinter
- Add scheduled notifications
- Sort notifications by date and time
- Add recurring notifications
- Store data in JSON or SQLite
- Add edit reminder action
- Filter by status
- Add unit tests
## Author
A Python learning exercise to practice building a small real-world CLI application.