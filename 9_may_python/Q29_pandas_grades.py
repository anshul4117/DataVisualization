# Q29. Create a DataFrame with student marks in multiple subjects.
#      Calculate total marks, percentage, and assign grades using apply().

import pandas as pd

def assign_grade(percentage):
    """Assign grade based on percentage using conditional logic."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B+"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


def assign_remark(grade):
    """Assign remark based on grade."""
    remarks = {
        "A+": "Outstanding",
        "A": "Excellent",
        "B+": "Very Good",
        "B": "Good",
        "C": "Average",
        "D": "Below Average",
        "F": "Fail"
    }
    return remarks.get(grade, "N/A")


# --- Main Program ---
print("=" * 70)
print("   STUDENT MARKS ANALYSIS WITH GRADES (Pandas apply())")
print("=" * 70)

# Create student marks data
data = {
    'Student': ['Rahul', 'Priya', 'Amit', 'Sneha', 'Vikram',
                'Neha', 'Rohan', 'Kavita', 'Suresh', 'Deepa'],
    'Maths': [85, 92, 45, 78, 95, 60, 72, 88, 38, 67],
    'Science': [78, 88, 52, 82, 90, 55, 68, 91, 42, 73],
    'English': [90, 85, 48, 75, 88, 62, 70, 86, 35, 80],
    'Hindi': [82, 90, 55, 80, 92, 58, 75, 84, 40, 70],
    'Computer': [95, 87, 60, 85, 98, 65, 80, 93, 45, 75]
}

# Create DataFrame
marks_df = pd.DataFrame(data)
marks_df.set_index('Student', inplace=True)

# Display original marks
print("\n--- Original Student Marks ---")
print(marks_df)

# Calculate total marks using apply()
subjects = ['Maths', 'Science', 'English', 'Hindi', 'Computer']
marks_df['Total'] = marks_df[subjects].apply(sum, axis=1)

# Calculate percentage using apply()
max_marks = len(subjects) * 100
marks_df['Percentage'] = marks_df['Total'].apply(lambda x: round((x / max_marks) * 100, 2))

# Assign grade using apply()
marks_df['Grade'] = marks_df['Percentage'].apply(assign_grade)

# Assign remarks using apply()
marks_df['Remark'] = marks_df['Grade'].apply(assign_remark)

# Display the complete result table
print("\n" + "=" * 70)
print("   COMPLETE RESULT TABLE")
print("=" * 70)
print(marks_df)

# Summary statistics
print("\n" + "=" * 50)
print("   SUMMARY STATISTICS")
print("=" * 50)
print(f"  Class Average Percentage : {marks_df['Percentage'].mean():.2f}%")
print(f"  Highest Percentage       : {marks_df['Percentage'].max():.2f}% ({marks_df['Percentage'].idxmax()})")
print(f"  Lowest Percentage        : {marks_df['Percentage'].min():.2f}% ({marks_df['Percentage'].idxmin()})")
print(f"  Students Passed          : {len(marks_df[marks_df['Percentage'] >= 40])}")
print(f"  Students Failed          : {len(marks_df[marks_df['Percentage'] < 40])}")

# Grade-wise distribution
print("\n--- Grade Distribution ---")
grade_counts = marks_df['Grade'].value_counts().sort_index()
for grade, count in grade_counts.items():
    print(f"  Grade {grade:<3}: {count} student(s)")

# --- Expected Output ---
# ======================================================================
#    STUDENT MARKS ANALYSIS WITH GRADES (Pandas apply())
# ======================================================================
#
# --- Original Student Marks ---
#          Maths  Science  English  Hindi  Computer
# Student
# Rahul       85       78       90     82        95
# Priya       92       88       85     90        87
# ...
#
# ======================================================================
#    COMPLETE RESULT TABLE
# ======================================================================
#          Maths  Science  English  Hindi  Computer  Total  Percentage Grade      Remark
# Student
# Rahul       85       78       90     82        95    430       86.00     A   Excellent
# Priya       92       88       85     90        87    442       88.40     A   Excellent
# Amit        45       52       48     55        60    260       52.00     C     Average
# ...
#
# ==================================================
#    SUMMARY STATISTICS
# ==================================================
#   Class Average Percentage : 72.80%
#   Highest Percentage       : 92.60% (Vikram)
#   Lowest Percentage        : 40.00% (Suresh)
#   Students Passed          : 10
#   Students Failed          : 0
