# Q35. Contact management system using list and dictionary where users
#      can add, update, search, and delete contacts.

def display_menu():
    """Display the contact management menu."""
    print("\n" + "=" * 45)
    print("   CONTACT MANAGEMENT SYSTEM")
    print("=" * 45)
    print("  1. Add Contact")
    print("  2. Update Contact")
    print("  3. Search Contact")
    print("  4. Delete Contact")
    print("  5. Display All Contacts")
    print("  6. Exit")
    print("=" * 45)


def add_contact(contacts):
    """Add a new contact to the system."""
    name = input("  Enter Contact Name: ").strip().title()

    # Check if contact already exists
    for contact in contacts:
        if contact['name'] == name:
            print(f"  ⚠️ Contact '{name}' already exists. Use 'Update' instead.")
            return

    phone = input("  Enter Phone Number: ").strip()
    email = input("  Enter Email Address: ").strip()
    city = input("  Enter City: ").strip()

    # Create contact dictionary and add to list
    new_contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'city': city
    }
    contacts.append(new_contact)
    print(f"  ✅ Contact '{name}' added successfully!")


def update_contact(contacts):
    """Update an existing contact."""
    name = input("  Enter Contact Name to update: ").strip().title()

    for contact in contacts:
        if contact['name'] == name:
            print(f"\n  Current details of '{name}':")
            print(f"    Phone : {contact['phone']}")
            print(f"    Email : {contact['email']}")
            print(f"    City  : {contact['city']}")

            print("\n  Enter new details (press Enter to keep current):")
            new_phone = input(f"    New Phone [{contact['phone']}]: ").strip()
            new_email = input(f"    New Email [{contact['email']}]: ").strip()
            new_city = input(f"    New City [{contact['city']}]: ").strip()

            # Update only if new value is provided
            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email
            if new_city:
                contact['city'] = new_city

            print(f"  ✅ Contact '{name}' updated successfully!")
            return

    print(f"  ❌ Contact '{name}' not found.")


def search_contact(contacts):
    """Search for a contact by name."""
    search_term = input("  Enter name to search: ").strip().lower()

    found = []
    for contact in contacts:
        if search_term in contact['name'].lower():
            found.append(contact)

    if found:
        print(f"\n  Found {len(found)} matching contact(s):")
        print(f"  {'Name':<18} {'Phone':<15} {'Email':<25} {'City':<12}")
        print("  " + "-" * 65)
        for contact in found:
            print(f"  {contact['name']:<18} {contact['phone']:<15} {contact['email']:<25} {contact['city']:<12}")
    else:
        print(f"  ❌ No contacts found matching '{search_term}'.")


def delete_contact(contacts):
    """Delete a contact from the system."""
    name = input("  Enter Contact Name to delete: ").strip().title()

    for i, contact in enumerate(contacts):
        if contact['name'] == name:
            confirm = input(f"  Are you sure you want to delete '{name}'? (yes/no): ").strip().lower()
            if confirm in ['yes', 'y']:
                contacts.pop(i)
                print(f"  ✅ Contact '{name}' deleted successfully!")
            else:
                print("  Deletion cancelled.")
            return

    print(f"  ❌ Contact '{name}' not found.")


def display_all_contacts(contacts):
    """Display all contacts in the system."""
    if not contacts:
        print("\n  📭 No contacts found. Add some contacts first!")
        return

    print(f"\n  --- All Contacts ({len(contacts)} total) ---")
    print(f"  {'#':<4} {'Name':<18} {'Phone':<15} {'Email':<25} {'City':<12}")
    print("  " + "-" * 72)
    for idx, contact in enumerate(contacts, 1):
        print(f"  {idx:<4} {contact['name']:<18} {contact['phone']:<15} {contact['email']:<25} {contact['city']:<12}")


# --- Main Program ---
print("\n" + "=" * 45)
print("   WELCOME TO CONTACT MANAGER")
print("=" * 45)

# Initialize contact list
contact_list = []

# Menu-driven loop
while True:
    display_menu()
    user_choice = input("  Enter your choice (1-6): ").strip()

    if user_choice == '1':
        add_contact(contact_list)
    elif user_choice == '2':
        update_contact(contact_list)
    elif user_choice == '3':
        search_contact(contact_list)
    elif user_choice == '4':
        delete_contact(contact_list)
    elif user_choice == '5':
        display_all_contacts(contact_list)
    elif user_choice == '6':
        print(f"\n  Total contacts saved: {len(contact_list)}")
        print("  Thank you for using Contact Manager! Goodbye!")
        break
    else:
        print("  ❌ Invalid choice. Please enter 1-6.")

# --- Expected Output ---
# =============================================
#    WELCOME TO CONTACT MANAGER
# =============================================
#
# =============================================
#    CONTACT MANAGEMENT SYSTEM
# =============================================
#   1. Add Contact
#   2. Update Contact
#   3. Search Contact
#   4. Delete Contact
#   5. Display All Contacts
#   6. Exit
# =============================================
#   Enter your choice (1-6): 1
#   Enter Contact Name: Rahul Sharma
#   Enter Phone Number: 9876543210
#   Enter Email Address: rahul@email.com
#   Enter City: Mumbai
#   ✅ Contact 'Rahul Sharma' added successfully!
#
#   Enter your choice (1-6): 5
#   --- All Contacts (1 total) ---
#   #    Name               Phone           Email                     City
#   ------------------------------------------------------------------------
#   1    Rahul Sharma       9876543210      rahul@email.com           Mumbai
#
#   Enter your choice (1-6): 6
#   Total contacts saved: 1
#   Thank you for using Contact Manager! Goodbye!
