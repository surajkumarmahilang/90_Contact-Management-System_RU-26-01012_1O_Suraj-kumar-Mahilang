contacts = []


def add_contact():
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()

    if len(phone) != 10 or not phone.isdigit():
        print("Invalid phone number. Enter exactly 10 digits.")
        return

    for c in contacts:
        if c["phone"] == phone:
            print("Contact with this number already exists.")
            return

    email = input("Enter Email (press Enter to skip): ").strip()

    new_contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(new_contact)
    print("Contact added: " + name + " | " + phone)


def view_contacts():
    if len(contacts) == 0:
        print("No contacts found.")
        return

    print("\n--- Contact List ---")
    for c in contacts:
        if c["email"] != "":
            print(c["name"] + " | " + c["phone"] + " | " + c["email"])
        else:
            print(c["name"] + " | " + c["phone"])


def search_contact():
    search_name = input("Enter Name to search: ").strip().lower()
    found = False

    for c in contacts:
        if search_name in c["name"].lower():
            if c["email"] != "":
                print(c["name"] + " | " + c["phone"] + " | " + c["email"])
            else:
                print(c["name"] + " | " + c["phone"])
            found = True

    if not found:
        print("Contact not found.")


def update_contact():
    name = input("Enter Name to update: ").strip().lower()

    for c in contacts:
        if c["name"].lower() == name:
            new_phone = input("Enter new 10-digit Phone Number: ").strip()

            if len(new_phone) != 10 or not new_phone.isdigit():
                print("Invalid phone number. Enter exactly 10 digits.")
                return

            for other in contacts:
                if other["phone"] == new_phone and other != c:
                    print("Contact with this number already exists.")
                    return

            c["phone"] = new_phone
            print("Phone updated: " + new_phone)
            return

    print("Contact not found.")


def delete_contact():
    name = input("Enter Name to delete: ").strip().lower()

    for c in contacts:
        if c["name"].lower() == name:
            deleted_name = c["name"]
            contacts.remove(c)
            print("Contact '" + deleted_name + "' deleted. Total contacts: " + str(len(contacts)))
            return

    print("Contact not found.")


while True:
    print("\n--- Contact Management System ---")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please enter 1 to 6.")