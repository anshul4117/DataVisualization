# Q32. Validate user age for voting eligibility and handle invalid
#      numeric and non-numeric inputs gracefully.

def get_valid_age():
    """Get a valid age input from the user with error handling."""
    while True:
        user_input = input("  Enter your age: ").strip()

        try:
            # Try to convert input to a number
            age = float(user_input)

            # Check for non-numeric characters that float() might miss
            if age != int(age):
                print("  ⚠️  Age must be a whole number, not a decimal.")
                continue

            age = int(age)

            # Validate age range
            if age < 0:
                raise ValueError("Age cannot be negative.")
            elif age > 150:
                raise ValueError("Age seems unrealistic. Please enter a valid age.")
            elif age == 0:
                raise ValueError("Age cannot be zero.")

            return age

        except ValueError as ve:
            if "could not convert" in str(ve) or "invalid literal" in str(ve):
                print(f"  ❌ Non-numeric input detected: '{user_input}'")
                print("     Please enter a valid number.")
            else:
                print(f"  ❌ Invalid Input: {ve}")


def check_voting_eligibility(age):
    """Check voting eligibility based on age."""
    min_voting_age = 18

    if age >= min_voting_age:
        years_eligible = age - min_voting_age
        return True, years_eligible
    else:
        years_remaining = min_voting_age - age
        return False, years_remaining


# --- Main Program ---
print("=" * 55)
print("   VOTING ELIGIBILITY CHECKER")
print("   (with Input Validation)")
print("=" * 55)

while True:
    print("\n" + "-" * 40)

    # Get valid age
    user_age = get_valid_age()

    # Check eligibility
    is_eligible, years = check_voting_eligibility(user_age)

    # Display result
    print(f"\n  Your Age: {user_age} years")
    if is_eligible:
        print(f"  ✅ You ARE eligible to vote!")
        if years > 0:
            print(f"  📌 You have been eligible for {years} year(s).")
        else:
            print(f"  📌 Congratulations! You just became eligible this year!")
    else:
        print(f"  ❌ You are NOT eligible to vote yet.")
        print(f"  📌 You need to wait {years} more year(s).")
        print(f"  📌 You will be eligible in the year {2026 + years}.")

    # Ask to continue
    again = input("\n  Check another age? (yes/no): ").strip().lower()
    if again not in ['yes', 'y']:
        print("\n  Thank you for using the Voting Eligibility Checker!")
        break

# --- Expected Output ---
# =======================================================
#    VOTING ELIGIBILITY CHECKER
#    (with Input Validation)
# =======================================================
#
# ----------------------------------------
#   Enter your age: abc
#   ❌ Non-numeric input detected: 'abc'
#      Please enter a valid number.
#   Enter your age: -5
#   ❌ Invalid Input: Age cannot be negative.
#   Enter your age: 16.5
#   ⚠️  Age must be a whole number, not a decimal.
#   Enter your age: 20
#
#   Your Age: 20 years
#   ✅ You ARE eligible to vote!
#   📌 You have been eligible for 2 year(s).
#
#   Check another age? (yes/no): yes
#
# ----------------------------------------
#   Enter your age: 15
#
#   Your Age: 15 years
#   ❌ You are NOT eligible to vote yet.
#   📌 You need to wait 3 more year(s).
#   📌 You will be eligible in the year 2029.
#
#   Check another age? (yes/no): no
#   Thank you for using the Voting Eligibility Checker!
