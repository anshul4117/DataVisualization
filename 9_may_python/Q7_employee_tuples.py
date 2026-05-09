# Q7. Store employee records in tuples (ID, Name, Salary) and display
#     employees whose salary is above the average salary.

def get_employee_records():
    """Accept employee records from the user and store in tuples."""
    records = []
    try:
        num_employees = int(input("Enter the number of employees: "))
    except ValueError:
        print("Invalid input. Using default 3 employees.")
        num_employees = 3

    for i in range(1, num_employees + 1):
        print(f"\n--- Employee {i} ---")
        emp_id = input("  Enter Employee ID: ")
        emp_name = input("  Enter Employee Name: ")
        while True:
            try:
                emp_salary = float(input("  Enter Employee Salary: Rs. "))
                break
            except ValueError:
                print("  Invalid salary. Please enter a numeric value.")

        # Store each record as a tuple
        employee_tuple = (emp_id, emp_name, emp_salary)
        records.append(employee_tuple)

    return records


def calculate_average_salary(records):
    """Calculate the average salary from employee records."""
    total_salary = 0
    for record in records:
        total_salary += record[2]  # Salary is at index 2
    average = total_salary / len(records)
    return average


def display_above_average(records, avg_salary):
    """Display employees whose salary is above the average."""
    above_avg_employees = []
    for record in records:
        if record[2] > avg_salary:
            above_avg_employees.append(record)
    return above_avg_employees


# --- Main Program ---
print("=" * 55)
print("   EMPLOYEE RECORDS MANAGEMENT (TUPLES)")
print("=" * 55)

# Get employee records
employee_records = get_employee_records()

# Calculate average salary
average_salary = calculate_average_salary(employee_records)

# Display all employees
print("\n" + "=" * 55)
print("   ALL EMPLOYEE RECORDS")
print("=" * 55)
print(f"{'ID':<10} {'Name':<20} {'Salary':>12}")
print("-" * 45)
for record in employee_records:
    print(f"{record[0]:<10} {record[1]:<20} Rs. {record[2]:>8.2f}")

print(f"\nAverage Salary: Rs. {average_salary:.2f}")

# Display employees above average salary
above_average = display_above_average(employee_records, average_salary)

print("\n" + "=" * 55)
print("   EMPLOYEES WITH SALARY ABOVE AVERAGE")
print("=" * 55)
if above_average:
    print(f"{'ID':<10} {'Name':<20} {'Salary':>12}")
    print("-" * 45)
    for record in above_average:
        print(f"{record[0]:<10} {record[1]:<20} Rs. {record[2]:>8.2f}")
else:
    print("  No employees found above average salary.")

# --- Expected Output ---
# =======================================================
#    EMPLOYEE RECORDS MANAGEMENT (TUPLES)
# =======================================================
# Enter the number of employees: 4
#
# --- Employee 1 ---
#   Enter Employee ID: E001
#   Enter Employee Name: Rahul
#   Enter Employee Salary: Rs. 45000
#
# --- Employee 2 ---
#   Enter Employee ID: E002
#   Enter Employee Name: Priya
#   Enter Employee Salary: Rs. 55000
#
# --- Employee 3 ---
#   Enter Employee ID: E003
#   Enter Employee Name: Amit
#   Enter Employee Salary: Rs. 35000
#
# --- Employee 4 ---
#   Enter Employee ID: E004
#   Enter Employee Name: Sneha
#   Enter Employee Salary: Rs. 65000
#
# =======================================================
#    ALL EMPLOYEE RECORDS
# =======================================================
# ID         Name                       Salary
# ---------------------------------------------
# E001       Rahul                Rs. 45000.00
# E002       Priya                Rs. 55000.00
# E003       Amit                 Rs. 35000.00
# E004       Sneha                Rs. 65000.00
#
# Average Salary: Rs. 50000.00
#
# =======================================================
#    EMPLOYEES WITH SALARY ABOVE AVERAGE
# =======================================================
# ID         Name                       Salary
# ---------------------------------------------
# E002       Priya                Rs. 55000.00
# E004       Sneha                Rs. 65000.00
