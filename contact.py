# Simple Contact Manager in Python

def display_menu():
    print("\n--- Contact Manager ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    phone = input("Enter contact phone number: ").strip()
    email = input("Enter contact email: ").strip()
    address = input("Enter contact address: ").strip()
    
    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    
    print(f"\nContact {name} added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("\nNo contacts found.")
        return
    
    print("\n--- Contact List ---")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}")

def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ").strip()
    
    results = {name: details for name, details in contacts.items()
               if search_term.lower() in name.lower() or search_term in details['phone']}
    
    if results:
        print("\n--- Search Results ---")
        for name, details in results.items():
            print(f"\nName: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
    else:
        print("\nNo matching contacts found.")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ").strip()
    
    if name in contacts:
        print("\n--- Current Details ---")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
        print(f"Address: {contacts[name]['address']}")
        
        phone = input("Enter new phone number (leave blank to keep current): ").strip()
        email = input("Enter new email (leave blank to keep current): ").strip()
        address = input("Enter new address (leave blank to keep current): ").strip()
        
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        if address:
            contacts[name]['address'] = address
        
        print(f"\nContact {name} updated successfully.")
    else:
        print("\nContact not found.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()
    
    if name in contacts:
        del contacts[name]
        print(f"\nContact {name} deleted successfully.")
    else:
        print("\nContact not found.")

def main():
    contacts = {}
    
    while True:
        display_menu()
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the Contact Manager
if __name__ == "__main__":
    main()
