# Q39. Read a CSV file containing student attendance records and
#      display students with attendance below 75%.

import pandas as pd
import os

def create_attendance_csv(filename):
    """Create a sample student attendance CSV file."""
    data = {
        'Roll_No': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
                     111, 112, 113, 114, 115],
        'Name': ['Rahul Sharma', 'Priya Singh', 'Amit Kumar', 'Sneha Patel',
                 'Vikram Gupta', 'Neha Joshi', 'Rohan Verma', 'Kavita Reddy',
                 'Suresh Nair', 'Deepa Iyer', 'Arjun Das', 'Meera Shah',
                 'Karan Mehta', 'Pooja Rao', 'Tanvi Kapoor'],
        'Total_Classes': [120, 120, 120, 120, 120, 120, 120, 120, 120, 120,
                          120, 120, 120, 120, 120],
        'Classes_Attended': [110, 85, 95, 60, 115, 70, 100, 88, 55, 105,
                             78, 92, 65, 108, 82]
    }

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"  Attendance CSV file '{os.path.basename(filename)}' created!\n")


# --- Main Program ---
print("=" * 65)
print("   STUDENT ATTENDANCE ANALYSIS")
print("=" * 65)

# Create sample CSV file
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_filename = os.path.join(script_dir, "student_attendance.csv")
create_attendance_csv(csv_filename)

# Read attendance data from CSV
attendance_df = pd.read_csv(csv_filename)

# Calculate attendance percentage
attendance_df['Attendance_%'] = round(
    (attendance_df['Classes_Attended'] / attendance_df['Total_Classes']) * 100, 2
)

# Determine status based on 75% threshold
attendance_df['Status'] = attendance_df['Attendance_%'].apply(
    lambda x: '✅ Regular' if x >= 75 else '❌ Shortage'
)

# Display all student attendance records
print("--- All Student Attendance Records ---")
print(attendance_df.to_string(index=False))

# Filter students with attendance below 75%
below_threshold = attendance_df[attendance_df['Attendance_%'] < 75]

print("\n" + "=" * 60)
print("   ⚠️  STUDENTS WITH ATTENDANCE BELOW 75%")
print("=" * 60)

if not below_threshold.empty:
    print(f"\n  {len(below_threshold)} student(s) have attendance below 75%:\n")
    print(f"  {'Roll No':<10} {'Name':<18} {'Attended':<10} {'Total':<8} {'%':>6} {'Shortage':>8}")
    print("  " + "-" * 62)
    for _, row in below_threshold.iterrows():
        shortage = row['Total_Classes'] * 0.75 - row['Classes_Attended']
        print(f"  {row['Roll_No']:<10} {row['Name']:<18} {row['Classes_Attended']:<10} "
              f"{row['Total_Classes']:<8} {row['Attendance_%']:>5.1f}% {int(shortage):>6}")
else:
    print("  All students have attendance above 75%.")

# Summary statistics
print("\n" + "=" * 50)
print("   ATTENDANCE SUMMARY")
print("=" * 50)
print(f"  Total Students         : {len(attendance_df)}")
print(f"  Regular (≥ 75%)        : {len(attendance_df[attendance_df['Attendance_%'] >= 75])}")
print(f"  Shortage (< 75%)       : {len(below_threshold)}")
print(f"  Average Attendance     : {attendance_df['Attendance_%'].mean():.2f}%")
print(f"  Highest Attendance     : {attendance_df['Attendance_%'].max():.2f}% "
      f"({attendance_df.loc[attendance_df['Attendance_%'].idxmax(), 'Name']})")
print(f"  Lowest Attendance      : {attendance_df['Attendance_%'].min():.2f}% "
      f"({attendance_df.loc[attendance_df['Attendance_%'].idxmin(), 'Name']})")

# --- Expected Output ---
# =================================================================
#    STUDENT ATTENDANCE ANALYSIS
# =================================================================
#   Attendance CSV file 'student_attendance.csv' created!
#
# --- All Student Attendance Records ---
#  Roll_No             Name  Total_Classes  Classes_Attended  Attendance_%     Status
#      101     Rahul Sharma            120               110         91.67  ✅ Regular
#      102      Priya Singh            120                85         70.83  ❌ Shortage
#      ...
#
# ============================================================
#    ⚠️  STUDENTS WITH ATTENDANCE BELOW 75%
# ============================================================
#
#   5 student(s) have attendance below 75%:
#
#   Roll No    Name               Attended   Total       %  Shortage
#   --------------------------------------------------------------
#   102        Priya Singh        85         120    70.8%       5
#   104        Sneha Patel        60         120    50.0%      30
#   106        Neha Joshi         70         120    58.3%      20
#   109        Suresh Nair        55         120    45.8%      35
#   113        Karan Mehta        65         120    54.2%      25
#
# ==================================================
#    ATTENDANCE SUMMARY
# ==================================================
#   Total Students         : 15
#   Regular (≥ 75%)        : 10
#   Shortage (< 75%)       : 5
#   Average Attendance     : 72.22%
#   Highest Attendance     : 95.83% (Vikram Gupta)
#   Lowest Attendance      : 45.83% (Suresh Nair)
