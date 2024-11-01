import os
import json

def load_notes(username, is_admin=False):
    if is_admin:
        return {user: load_user_notes(user) for user in get_all_users()}
    return load_user_notes(username)

def load_user_notes(username):
    filename = f"{username}_notes.json"
    return json.load(open(filename, 'r')) if os.path.exists(filename) else {}

def save_notes(username, notes):
    with open(f"{username}_notes.json", 'w') as file:
        json.dump(notes, file)

def register_user():
    username = input("Enter a username: ")
    passcode = input("Enter a passcode: ")
    role = input("Enter role (user/admin): ").strip().lower()
    if role not in ['user', 'admin']:
        print("Invalid role. Defaulting to user.")
        role = 'user'
    with open("users.json", 'a') as file:
        file.write(f"{username}:{passcode}:{role}\n")
    print("User registered successfully!")

def authenticate_user():
    username = input("Enter your username: ")
    passcode = input("Enter your passcode: ")
    with open("users.json", 'r') as file:
        for line in file:
            stored_username, stored_passcode, role = line.strip().split(':')
            if stored_username == username and stored_passcode == passcode:
                print("Login successful!")
                return username, role
    print("Invalid username or passcode.")
    return None, None

def get_all_users():
    if not os.path.exists("users.json"):
        return []
    with open("users.json", 'r') as file:
        return [line.split(':')[0] for line in file]

def add_note(notes):
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    notes[title] = content
    print("Note added successfully!")

def view_notes(notes, is_admin):
    if is_admin:
        for user, user_notes in notes.items():
            print(f"\nNotes for {user}:")
            display_notes(user_notes)
    else:
        display_notes(notes)

def display_notes(notes):
    if notes:
        for title, content in notes.items():
            print(f"Title: {title}\nContent: {content}\n" + "-" * 20)
    else:
        print("No notes found.")

def delete_note(notes):
    title = input("Enter title of note to delete: ")
    if title in notes:
        del notes[title]
        print(f"Note '{title}' deleted successfully!")
    else:
        print(f"Note '{title}' not found.")

def main_menu(username, is_admin):
    notes = load_notes(username, is_admin)
    while True:
        print("\nNOTE-FY")
        print("1. Add a Note")
        print("2. View All Notes" if is_admin else "2. View My Notes")
        print("3. Delete a Note")
        print("4. Save and Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            add_note(notes)
        elif choice == '2':
            view_notes(notes, is_admin)
        elif choice == '3':
            delete_note(notes)
        elif choice == '4':
            save_notes(username, notes)
            print("Notes saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    action = input("Do you want to (1) Register or (2) Login? ")
    if action == '1':
        register_user()
    elif action == '2':
        username, role = authenticate_user()
        if username:
            is_admin = role == 'admin'
            main_menu(username, is_admin)
    else:
        print("Invalid choice.")
