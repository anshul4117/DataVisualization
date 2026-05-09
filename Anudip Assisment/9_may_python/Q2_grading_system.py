# Q2. Grading system with percentage calculation, grade assignment using
#     nested if-else, and scholarship eligibility check.

def get_marks():
    """Accept marks for five subjects from the user."""
    subjects = ["Mathematics", "Science", "English", "Computer Science", "Hindi"]
    marks_list = []

    print("\nEnter marks for the following subjects (out of 100):")
    for subject in subjects:
        while True:
            try:
                mark = float(input(f"  {subject}: "))
                if 0 <= mark <= 100:
                    marks_list.append(mark)
                    break
                else:
                    print("  Marks must be between 0 and 100. Try again.")
            except ValueError:
                print("  Invalid input. Please enter a numeric value.")

    return subjects, marks_list


def calculate_percentage(marks_list):
    """Calculate the percentage from the list of marks."""
    total_marks = sum(marks_list)
    percentage = total_marks / len(marks_list)
    return total_marks, percentage


def assign_grade(percentage):
    """Assign grade using nested if-else conditions."""
    if percentage >= 90:
        if percentage >= 95:
            grade = "A+"
        else:
            grade = "A"
    elif percentage >= 80:
        if percentage >= 85:
            grade = "B+"
        else:
            grade = "B"
    elif percentage >= 70:
        if percentage >= 75:
            grade = "C+"
        else:
            grade = "C"
    elif percentage >= 60:
        if percentage >= 65:
            grade = "D+"
        else:
            grade = "D"
    elif percentage >= 50:
        grade = "E"
    else:
        grade = "F (Fail)"

    return grade


def check_scholarship(percentage, marks_list):
    """Check if the student qualifies for a scholarship."""
    # Scholarship criteria: percentage >= 85 and no subject below 70
    if percentage >= 85:
        if all(mark >= 70 for mark in marks_list):
            return True, "Merit Scholarship (All subjects above 70, percentage >= 85%)"
        else:
            return False, "Does not qualify: Some subjects are below 70 marks"
    elif percentage >= 75:
        if all(mark >= 60 for mark in marks_list):
            return True, "Partial Scholarship (All subjects above 60, percentage >= 75%)"
        else:
            return False, "Does not qualify: Some subjects are below 60 marks"
    else:
        return False, "Does not qualify: Percentage is below 75%"


# --- Main Program ---
print("=" * 55)
print("   STUDENT GRADING SYSTEM")
print("=" * 55)

# Get marks from user
subjects, marks = get_marks()

# Calculate percentage
total, percentage = calculate_percentage(marks)

# Assign grade
grade = assign_grade(percentage)

# Check scholarship eligibility
is_eligible, scholarship_message = check_scholarship(percentage, marks)

# Display the results
print("\n" + "=" * 55)
print("   RESULT CARD")
print("=" * 55)
for i in range(len(subjects)):
    print(f"  {subjects[i]:<20}: {marks[i]:>6.1f}")
print("-" * 35)
print(f"  {'Total Marks':<20}: {total:>6.1f} / {len(marks) * 100}")
print(f"  {'Percentage':<20}: {percentage:>6.2f}%")
print(f"  {'Grade':<20}: {grade}")
print("-" * 35)
print(f"  Scholarship Status : {'Eligible' if is_eligible else 'Not Eligible'}")
print(f"  Reason             : {scholarship_message}")
print("=" * 55)

# --- Expected Output ---
# =======================================================
#    STUDENT GRADING SYSTEM
# =======================================================
#
# Enter marks for the following subjects (out of 100):
#   Mathematics: 92
#   Science: 88
#   English: 95
#   Computer Science: 90
#   Hindi: 85
#
# =======================================================
#    RESULT CARD
# =======================================================
#   Mathematics         :   92.0
#   Science             :   88.0
#   English             :   95.0
#   Computer Science    :   90.0
#   Hindi               :   85.0
# -----------------------------------
#   Total Marks         :  450.0 / 500
#   Percentage          :  90.00%
#   Grade               : A
# -----------------------------------
#   Scholarship Status : Eligible
#   Reason             : Merit Scholarship (All subjects above 70, percentage >= 85%)
# =======================================================
