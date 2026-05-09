# Q15. Pandas program to read employee data from CSV and display
#      department-wise average salary and highest salary employee.

import pandas as pd
import os

def create_sample_csv(filename):
    """Create a sample employee CSV file for demonstration."""
    data = {
        'EmpID': ['E001', 'E002', 'E003', 'E004', 'E005',
                  'E006', 'E007', 'E008', 'E009', 'E010'],
        'Name': ['Rahul Sharma', 'Priya Singh', 'Amit Kumar', 'Sneha Patel',
                 'Vikram Gupta', 'Neha Joshi', 'Rohan Verma', 'Kavita Reddy',
                 'Suresh Nair', 'Deepa Iyer'],
        'Department': ['IT', 'HR', 'IT', 'Finance', 'IT',
                       'HR', 'Finance', 'IT', 'HR', 'Finance'],
        'Salary': [75000, 55000, 82000, 68000, 90000,
                   60000, 72000, 78000, 52000, 65000]
    }

    # Create DataFrame and save to CSV
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"  Sample CSV file '{filename}' created successfully!\n")
    return df


# --- Main Program ---
print("=" * 60)
print("   EMPLOYEE DATA ANALYSIS USING PANDAS")
print("=" * 60)

# Define the CSV filename
csv_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "employee_data.csv")

# Create sample CSV file
create_sample_csv(csv_filename)

# Read employee data from CSV
employee_df = pd.read_csv(csv_filename)

# Display all employee data
print("--- All Employee Records ---")
print(employee_df.to_string(index=False))
print(f"\nTotal Employees: {len(employee_df)}")

# 1. Department-wise Average Salary
print("\n" + "=" * 50)
print("   DEPARTMENT-WISE AVERAGE SALARY")
print("=" * 50)
dept_avg_salary = employee_df.groupby('Department')['Salary'].mean()
for dept, avg_sal in dept_avg_salary.items():
    print(f"  {dept:<15} : Rs. {avg_sal:>10,.2f}")

# 2. Highest Salary Employee (overall)
print("\n" + "=" * 50)
print("   HIGHEST SALARY EMPLOYEE (OVERALL)")
print("=" * 50)
max_salary_idx = employee_df['Salary'].idxmax()
top_employee = employee_df.loc[max_salary_idx]
print(f"  Employee ID   : {top_employee['EmpID']}")
print(f"  Name          : {top_employee['Name']}")
print(f"  Department    : {top_employee['Department']}")
print(f"  Salary        : Rs. {top_employee['Salary']:,.2f}")

# 3. Highest Salary Employee per Department
print("\n" + "=" * 50)
print("   HIGHEST SALARY EMPLOYEE PER DEPARTMENT")
print("=" * 50)
for dept in employee_df['Department'].unique():
    dept_df = employee_df[employee_df['Department'] == dept]
    top_in_dept = dept_df.loc[dept_df['Salary'].idxmax()]
    print(f"  {dept:<10} -> {top_in_dept['Name']:<18} Rs. {top_in_dept['Salary']:>10,.2f}")

# 4. Department-wise statistics
print("\n" + "=" * 50)
print("   DEPARTMENT-WISE STATISTICS")
print("=" * 50)
dept_stats = employee_df.groupby('Department')['Salary'].agg(['mean', 'min', 'max', 'count'])
print(dept_stats.to_string())

# --- Expected Output ---
# ============================================================
#    EMPLOYEE DATA ANALYSIS USING PANDAS
# ============================================================
#   Sample CSV file 'employee_data.csv' created successfully!
#
# --- All Employee Records ---
# EmpID           Name Department  Salary
#  E001   Rahul Sharma         IT   75000
#  E002    Priya Singh         HR   55000
#  E003     Amit Kumar         IT   82000
#  E004    Sneha Patel    Finance   68000
#  E005   Vikram Gupta         IT   90000
#  E006     Neha Joshi         HR   60000
#  E007   Rohan Verma     Finance   72000
#  E008   Kavita Reddy         IT   78000
#  E009    Suresh Nair         HR   52000
#  E010     Deepa Iyer    Finance   65000
#
# Total Employees: 10
#
# ==================================================
#    DEPARTMENT-WISE AVERAGE SALARY
# ==================================================
#   Finance         : Rs.  68,333.33
#   HR              : Rs.  55,666.67
#   IT              : Rs.  81,250.00
#
# ==================================================
#    HIGHEST SALARY EMPLOYEE (OVERALL)
# ==================================================
#   Employee ID   : E005
#   Name          : Vikram Gupta
#   Department    : IT
#   Salary        : Rs. 90,000.00
#
# ==================================================
#    HIGHEST SALARY EMPLOYEE PER DEPARTMENT
# ==================================================
#   IT         -> Vikram Gupta       Rs.  90,000.00
#   HR         -> Neha Joshi         Rs.  60,000.00
#   Finance    -> Rohan Verma        Rs.  72,000.00
#
# ==================================================
#    DEPARTMENT-WISE STATISTICS
# ==================================================
#                     mean    min    max  count
# Department
# Finance      68333.333333  65000  72000      3
# HR           55666.666667  52000  60000      3
# IT           81250.000000  75000  90000      4
