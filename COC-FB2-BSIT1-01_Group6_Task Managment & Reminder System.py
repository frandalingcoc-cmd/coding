# Online Python compiler (interpreter)
# Write and run Python online using this editor.

task_ids = []
task_records = []
ALLOWED_SUBJECTS = ["ITE260", "ITE366"]

def add_task(tid, subject, desc, due_year, due_month, due_day, due_hour):

    tid = tid.strip()
    if len(tid) == 0:
        print("\n[ERROR] Student ID cannot be empty!")
        return
    
    
    for char in tid:
        if not (char.isdigit() or char == '-'):
            print("\n[ERROR] Invalid Student ID!.")
            return
    
    
    if tid in task_ids:
        print(f"\n[ERROR] Student ID '{tid}' already exists! Use a unique ID.")
        return

    
    subject = subject.strip().upper()
    if subject not in ALLOWED_SUBJECTS:
        print(f"\n[ERROR] Invalid subject! Only {', '.join(ALLOWED_SUBJECTS)} are allowed.")
        return

    
    if not isinstance(due_year, int) or due_year < 2024 or due_year > 2100:
        print("\n[ERROR] Invalid year! Enter a valid year between 2024 and 2100.")
        return

   
    if not isinstance(due_month, int) or not (1 <= due_month <= 12):
        print("\n[ERROR] Invalid month! Enter a value from 1 to 12.")
        return

    
    if not isinstance(due_day, int) or not (1 <= due_day <= 31):
        print("\n[ERROR] Invalid day! Enter a value from 1 to 31.")
        return
    if due_month in [4, 6, 9, 11] and due_day > 30:
        print("\n[ERROR] Invalid day! This month has only up to 30 days.")
        return
    if due_month == 2 and due_day > 29:
        print("\n[ERROR] Invalid day! February has at most 29 days.")
        return

    
    if len(due_hour.strip()) == 0:
        print("\n[ERROR] Time cannot be empty! Please enter a valid time.")
        return

    
    task_ids.append(tid)
    task_records.append([
        tid,
        subject,
        desc,
        due_year,
        due_month,
        due_day,
        due_hour,
        False
    ])
    print(
        f"\n[SUCCESS] Task added for Student ID {tid} ({subject}) "
        f"due: {due_year}-{due_month:02d}-{due_day:02d} @ {due_hour}"
    )

def mark_complete(tid):
    tid = tid.strip()
    if tid not in task_ids:
        print(f"\n[ERROR] Student ID '{tid}' not found in the system.")
        return
    for record in task_records:
        if record[0] == tid and record[7] == False:
            record[7] = True
            print(f"[SUCCESS] Task for Student ID {tid} marked as COMPLETE!")
            return
    print(f"\n[ERROR] Task for Student ID {tid} is already COMPLETE.")

def view_task():
    print("\n" + "=" * 80)
    print(
        f"{'Student ID':<15}"
        f"{'Subject':<12}"
        f"{'Description':<25}"
        f"{'Due Date & Time':<25}"
        f"Status"
    )
    print("-" * 80)
    if len(task_records) == 0:
        print("No tasks recorded yet.")
    else:
        for rec in task_records:
            status = "COMPLETE" if rec[7] else "PENDING"
            due_info = f"{rec[3]}-{rec[4]:02d}-{rec[5]:02d} @ {rec[6]}"
            print(
                f"{rec[0]:<15}"
                f"{rec[1]:<12}"
                f"{rec[2]:<25}"
                f"{due_info:<25}"
                f"{status}"
            )
    print("=" * 80)

def check_reminders(current_year, current_month, current_day):
    if not isinstance(current_year, int) or current_year < 2024:
        print("\n[ERROR] Invalid year entered.")
        return
    if not (1 <= current_month <= 12):
        print("\n[ERROR] Invalid month entered.")
        return
    if not (1 <= current_day <= 31):
        print("\n[ERROR] Invalid day entered.")
        return

    print("\n--- UPCOMING DEADLINE REMINDERS ---")
    found = False
    for rec in task_records:
        if not rec[7] and rec[3] == current_year and rec[4] == current_month:
            days_left = rec[5] - current_day
            if 0 <= days_left <= 3:
                print(
                    f"WARNING: ID {rec[0]} — due in {days_left} day(s)! "
                    f"{rec[1]}: {rec[2]}"
                )
                found = True
    if not found:
        print("No upcoming deadlines within 3 days.")

def main():
    while True:
        print("\n===== IT STUDENT TASK MANAGEMENT SYSTEM =====")
        print("[1] Add New Task")
        print("[2] Mark Task as Completed")
        print("[3] View All Student Tasks")
        print("[4] Check Deadline Reminders")
        print("[5] Exit System")
        print("=" * 50)
        choice = input("Select an option (1-5): ")

        if choice == "1":
            print("\n--- Enter Student Details ---")
            tid = input("Enter Student ID (numbers & dashes only, e.g., 2024-0001): ").strip()
            subject = input("Enter Subject (ITE260 or ITE366 only): ")
            desc = input("Enter Task Description: ").strip()

            try:
                year = int(input("Enter Due Year (e.g., 2026): "))
                month = int(input("Enter Due Month (1-12): "))
                day = int(input("Enter Due Date (day): "))
            except ValueError:
                print("\n[ERROR] Invalid input! Year, month, and day must be numbers.")
                continue

            hour = input("Enter Due Time (e.g., 8:00 AM): ").strip()

            add_task(tid, subject, desc, year, month, day, hour)

        elif choice == "2":
            tid = input("Enter Student ID to mark complete: ").strip()
            mark_complete(tid)

        elif choice == "3":
            view_task()

        elif choice == "4":
            try:
                today_year = int(input("Enter Today's Year: "))
                today_month = int(input("Enter Today's Month (1-12): "))
                today_day = int(input("Enter Today's Date (Day): "))
            except ValueError:
                print("\n[ERROR] Invalid input! Must enter valid numbers for date.")
                continue
            check_reminders(today_year, today_month, today_day)

        elif choice == "5":
            print("Exiting system. Have a great day!")
            break

        else:
            print("[ERROR] Invalid option! Please choose 1-5.")

if __name__ == "__main__":
    main()
