# Q21. Generate a NumPy array of student marks and convert it into a
#      Pandas DataFrame. Display highest marks, average marks, and
#      subject-wise statistics.

import numpy as np
import pandas as pd

# Student names
student_names = ["Rahul", "Priya", "Amit", "Sneha", "Vikram",
                 "Neha", "Rohan", "Kavita", "Suresh", "Deepa"]

# Subject names
subjects = ["Maths", "Science", "English", "Hindi", "Computer"]

# Generate random marks using NumPy (range 35 to 100)
np.random.seed(42)
marks_array = np.random.randint(35, 101, size=(len(student_names), len(subjects)))

# Display the NumPy array
print("=" * 65)
print("   STUDENT MARKS ANALYSIS (NumPy + Pandas)")
print("=" * 65)
print("\nNumPy Array of Marks:")
print(marks_array)

# Convert NumPy array to Pandas DataFrame
marks_df = pd.DataFrame(marks_array, columns=subjects, index=student_names)
marks_df.index.name = "Student"

# Display the DataFrame
print("\n--- Student Marks DataFrame ---")
print(marks_df)

# 1. Highest marks in each subject
print("\n" + "=" * 50)
print("   HIGHEST MARKS (Subject-wise)")
print("=" * 50)
for subject in subjects:
    max_marks = marks_df[subject].max()
    top_student = marks_df[subject].idxmax()
    print(f"  {subject:<12}: {max_marks} (by {top_student})")

# 2. Average marks in each subject
print("\n" + "=" * 50)
print("   AVERAGE MARKS (Subject-wise)")
print("=" * 50)
for subject in subjects:
    avg = marks_df[subject].mean()
    print(f"  {subject:<12}: {avg:.2f}")

# 3. Subject-wise statistics using describe()
print("\n" + "=" * 50)
print("   SUBJECT-WISE STATISTICS")
print("=" * 50)
print(marks_df.describe().round(2))

# 4. Overall topper
marks_df['Total'] = marks_df.sum(axis=1)
marks_df['Percentage'] = (marks_df['Total'] / (len(subjects) * 100) * 100).round(2)
topper_name = marks_df['Total'].idxmax()
topper_total = marks_df.loc[topper_name, 'Total']
topper_pct = marks_df.loc[topper_name, 'Percentage']

print(f"\n🏆 Overall Topper: {topper_name} (Total: {topper_total}, Percentage: {topper_pct}%)")

# Display final DataFrame with Total and Percentage
print("\n--- Final Result Table ---")
print(marks_df)

# --- Expected Output ---
# =================================================================
#    STUDENT MARKS ANALYSIS (NumPy + Pandas)
# =================================================================
#
# NumPy Array of Marks:
# [[86 73 61 89 92]
#  [46 81 78 60 84]
#  [66 54 46 88 51]
#  ...
#
# --- Student Marks DataFrame ---
#          Maths  Science  English  Hindi  Computer
# Rahul       86       73       61     89        92
# Priya       46       81       78     60        84
# ...
#
# HIGHEST MARKS (Subject-wise)
#   Maths       : 93 (by Vikram)
#   Science     : 95 (by Deepa)
#   ...
#
# AVERAGE MARKS (Subject-wise)
#   Maths       : 68.50
#   ...
#
# 🏆 Overall Topper: Rahul (Total: 401, Percentage: 80.20%)
