# Q40. Mini student management system using functions, dictionaries,
#      file handling, exception handling, and Pandas for report generation.

import os
import pandas as pd

# --- File path for persistent storage ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(SCRIPT_DIR, "student_database.csv")


def load_students():
    """Load student records from CSV file."""
    try:
        if os.path.exists(DATA_FILE):
            df = pd.read_csv(DATA_FILE)
            students = {}
            for _, row in df.iterrows():
                roll = str(row['Roll_No'])
                students[roll] = {
                    'name': row['Name'],
                    'maths': row['Maths'],
                    'science': row['Science'],
                    'english': row['English']
                }
            return students
        else:
            return {}
    except Exception as e:
        print(f"  ⚠️ Error loading data: {e}")
        return {}


def save_students(students):
    """Save student records to CSV file."""
    try:
        records = []
        for roll, info in students.items():
            records.append({
                'Roll_No': roll,
                'Name': info['name'],
                'Maths': info['maths'],
                'Science': info['science'],
                'English': info['english']
            })
        df = pd.DataFrame(records)
        df.to_csv(DATA_FILE, index=False)
    except Exception as e:
        print(f"  ❌ Error saving data: {e}")


def display_menu():
    """Display the student management system menu."""
    print("\n" + "=" * 50)
    print("   STUDENT MANAGEMENT SYSTEM")
    print("=" * 50)
    print("  1. Add Student")
    print("  2. View Student")
    print("  3. Update Student Marks")
    print("  4. Delete Student")
    print("  5. Display All Students")
    print("  6. Generate Report (Pandas)")
    print("  7. Search by Name")
    print("  8. Exit")
    print("=" * 50)


def add_student(students):
    """Add a new student record."""
    roll = input("  Enter Roll Number: ").strip()
    if roll in students:
        print(f"  ⚠️ Roll No. {roll} already exists!")
        return

    name = input("  Enter Student Name: ").strip().title()

    try:
        maths = float(input("  Enter Maths marks (0-100): "))
        science = float(input("  Enter Science marks (0-100): "))
        english = float(input("  Enter English marks (0-100): "))

        # Validate marks range
        for mark, subject in [(maths, 'Maths'), (science, 'Science'), (english, 'English')]:
            if not 0 <= mark <= 100:
                raise ValueError(f"{subject} marks must be between 0 and 100.")

    except ValueError as ve:
        print(f"  ❌ Invalid input: {ve}")
        return

    students[roll] = {
        'name': name,
        'maths': maths,
        'science': science,
        'english': english
    }
    save_students(students)
    print(f"  ✅ Student '{name}' (Roll: {roll}) added successfully!")


def view_student(students):
    """View a specific student's details."""
    roll = input("  Enter Roll Number: ").strip()
    if roll not in students:
        print(f"  ❌ Student with Roll No. {roll} not found.")
        return

    info = students[roll]
    total = info['maths'] + info['science'] + info['english']
    percentage = total / 3

    print(f"\n  --- Student Details ---")
    print(f"  Roll No   : {roll}")
    print(f"  Name      : {info['name']}")
    print(f"  Maths     : {info['maths']}")
    print(f"  Science   : {info['science']}")
    print(f"  English   : {info['english']}")
    print(f"  Total     : {total}")
    print(f"  Percentage: {percentage:.2f}%")
    print(f"  Grade     : {get_grade(percentage)}")


def get_grade(percentage):
    """Return grade based on percentage."""
    if percentage >= 90: return "A+"
    elif percentage >= 80: return "A"
    elif percentage >= 70: return "B+"
    elif percentage >= 60: return "B"
    elif percentage >= 50: return "C"
    elif percentage >= 40: return "D"
    else: return "F"


def update_student(students):
    """Update student marks."""
    roll = input("  Enter Roll Number to update: ").strip()
    if roll not in students:
        print(f"  ❌ Student with Roll No. {roll} not found.")
        return

    info = students[roll]
    print(f"  Updating marks for: {info['name']}")

    try:
        new_maths = input(f"  Maths [{info['maths']}]: ").strip()
        new_science = input(f"  Science [{info['science']}]: ").strip()
        new_english = input(f"  English [{info['english']}]: ").strip()

        if new_maths:
            info['maths'] = float(new_maths)
        if new_science:
            info['science'] = float(new_science)
        if new_english:
            info['english'] = float(new_english)

        save_students(students)
        print(f"  ✅ Marks updated for {info['name']}!")

    except ValueError:
        print("  ❌ Invalid marks entered.")


def delete_student(students):
    """Delete a student record."""
    roll = input("  Enter Roll Number to delete: ").strip()
    if roll not in students:
        print(f"  ❌ Student with Roll No. {roll} not found.")
        return

    name = students[roll]['name']
    confirm = input(f"  Delete '{name}' (Roll: {roll})? (yes/no): ").strip().lower()
    if confirm in ['yes', 'y']:
        del students[roll]
        save_students(students)
        print(f"  ✅ Student '{name}' deleted!")
    else:
        print("  Cancelled.")


def display_all(students):
    """Display all student records."""
    if not students:
        print("\n  📭 No students in the database.")
        return

    print(f"\n  {'Roll':<8} {'Name':<18} {'Maths':>6} {'Sci':>6} {'Eng':>6} {'Total':>6} {'%':>7} {'Grade':>6}")
    print("  " + "-" * 68)
    for roll, info in students.items():
        total = info['maths'] + info['science'] + info['english']
        pct = total / 3
        grade = get_grade(pct)
        print(f"  {roll:<8} {info['name']:<18} {info['maths']:>6.0f} {info['science']:>6.0f} "
              f"{info['english']:>6.0f} {total:>6.0f} {pct:>6.2f}% {grade:>5}")


def generate_report(students):
    """Generate a detailed report using Pandas."""
    if not students:
        print("\n  📭 No data to generate report.")
        return

    # Build DataFrame
    records = []
    for roll, info in students.items():
        total = info['maths'] + info['science'] + info['english']
        pct = total / 3
        records.append({
            'Roll_No': roll, 'Name': info['name'],
            'Maths': info['maths'], 'Science': info['science'],
            'English': info['english'], 'Total': total,
            'Percentage': round(pct, 2), 'Grade': get_grade(pct)
        })

    df = pd.DataFrame(records)

    print("\n" + "=" * 60)
    print("   📊 STUDENT REPORT (Generated via Pandas)")
    print("=" * 60)
    print(df.to_string(index=False))

    # Statistics
    print(f"\n  --- Class Statistics ---")
    print(f"  Total Students     : {len(df)}")
    print(f"  Class Average      : {df['Percentage'].mean():.2f}%")
    print(f"  Highest Percentage : {df['Percentage'].max():.2f}% ({df.loc[df['Percentage'].idxmax(), 'Name']})")
    print(f"  Lowest Percentage  : {df['Percentage'].min():.2f}% ({df.loc[df['Percentage'].idxmin(), 'Name']})")
    print(f"  Pass Count (≥40%)  : {len(df[df['Percentage'] >= 40])}")
    print(f"  Fail Count (<40%)  : {len(df[df['Percentage'] < 40])}")

    # Subject-wise analysis
    print(f"\n  --- Subject-wise Average ---")
    for subject in ['Maths', 'Science', 'English']:
        print(f"  {subject:<10}: {df[subject].mean():.2f}")

    # Grade distribution
    print(f"\n  --- Grade Distribution ---")
    grade_counts = df['Grade'].value_counts().sort_index()
    for grade, count in grade_counts.items():
        print(f"  Grade {grade:<3}: {count} student(s)")

    # Save report
    report_file = os.path.join(SCRIPT_DIR, "student_report.csv")
    df.to_csv(report_file, index=False)
    print(f"\n  📁 Report saved to '{os.path.basename(report_file)}'")


def search_by_name(students):
    """Search student by name."""
    search = input("  Enter name to search: ").strip().lower()
    found = False
    for roll, info in students.items():
        if search in info['name'].lower():
            total = info['maths'] + info['science'] + info['english']
            pct = total / 3
            print(f"  Found: Roll={roll}, Name={info['name']}, "
                  f"Total={total:.0f}, %={pct:.2f}%")
            found = True
    if not found:
        print(f"  ❌ No student found matching '{search}'.")


# --- Main Program ---
print("\n" + "=" * 50)
print("   🎓 STUDENT MANAGEMENT SYSTEM")
print("=" * 50)

# Load existing data
student_db = load_students()
print(f"  Loaded {len(student_db)} student record(s).\n")

while True:
    display_menu()
    choice = input("  Enter your choice (1-8): ").strip()

    if choice == '1':
        add_student(student_db)
    elif choice == '2':
        view_student(student_db)
    elif choice == '3':
        update_student(student_db)
    elif choice == '4':
        delete_student(student_db)
    elif choice == '5':
        display_all(student_db)
    elif choice == '6':
        generate_report(student_db)
    elif choice == '7':
        search_by_name(student_db)
    elif choice == '8':
        save_students(student_db)
        print(f"\n  💾 Data saved. Total students: {len(student_db)}")
        print("  Thank you for using Student Management System! 🎓")
        break
    else:
        print("  ❌ Invalid choice. Please enter 1-8.")

# --- Expected Output ---
# ==================================================
#    🎓 STUDENT MANAGEMENT SYSTEM
# ==================================================
#   Loaded 0 student record(s).
#
# ==================================================
#    STUDENT MANAGEMENT SYSTEM
# ==================================================
#   1. Add Student
#   2. View Student
#   3. Update Student Marks
#   4. Delete Student
#   5. Display All Students
#   6. Generate Report (Pandas)
#   7. Search by Name
#   8. Exit
# ==================================================
#   Enter your choice (1-8): 1
#   Enter Roll Number: 101
#   Enter Student Name: Rahul Sharma
#   Enter Maths marks (0-100): 85
#   Enter Science marks (0-100): 78
#   Enter English marks (0-100): 90
#   ✅ Student 'Rahul Sharma' (Roll: 101) added successfully!
#
#   Enter your choice (1-8): 6
#
# ============================================================
#    📊 STUDENT REPORT (Generated via Pandas)
# ============================================================
# Roll_No          Name  Maths  Science  English  Total  Percentage Grade
#     101  Rahul Sharma   85.0     78.0     90.0  253.0       84.33     A
#
#   --- Class Statistics ---
#   Total Students     : 1
#   Class Average      : 84.33%
#   ...
#
#   Enter your choice (1-8): 8
#   💾 Data saved. Total students: 1
#   Thank you for using Student Management System! 🎓
