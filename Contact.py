import json
import os

FILE = "contacts.json"
contacts = {}

# Load contacts from file if it exists
def load_contacts():
    global contacts
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            try:
                contacts = json.load(f)
            except json.JSONDecodeError:
                contacts = {}
    else:
        contacts = {}

# Save contacts to file
def save_contacts():
    with open(FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def start():
    print("###########################################")
    try:
        user = int(input("Enter 1 to add number\n"
                         "Enter 2 to view contacts\n"
                         "Enter 3 to remove a contact\n"
                         "Enter 4 to update a contact\n"))
        print("###########################################")
        return user
    except ValueError:
        print("Please enter a number from 1–4")
        return None

def add_contact(name, number):
    contacts[name] = number
    save_contacts()
    print(f"Added {name}: {number}")

def update_contact(name, number):
    if name in contacts:
        contacts[name] = number
        save_contacts()
        print(f"Updated {name} to {number}")
    else:
        print(f"{name} not found in contacts.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        save_contacts()
        print(f"Deleted {name}")
    else:
        print(f"{name} not found in contacts.")

def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("##### Contacts #####")
        for name, number in contacts.items():
            print(f"{name}: {number}")
        print("####################")

# Main program loop
load_contacts()

while True:
    choice = start()
    if choice == 1:
        print("You chose to add contact")
        name = input("Enter the name: ")
        number = input("Enter the phone no: ")
        add_contact(name, number)

    elif choice == 2:
        print("You chose to view contacts")
        view_contacts()

    elif choice == 3:
        print("You chose to delete contact")
        name = input("Enter the name you want to delete: ")
        delete_contact(name)

    elif choice == 4:
        print("You chose to update a contact")
        name = input("Enter the name you want to update: ")
        number = input("Enter the new number: ")
        update_contact(name, number)

    elif choice is None:
        continue

    else:
        print("Invalid operation")

    ans = input("Do you still want to continue? (y/n) ").lower()
    if ans == "n":
        break
