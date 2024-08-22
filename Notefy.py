notes = {}

def add_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    notes[title] = content
    print("Note added successfully!")

def view_notes():
    if notes:
        print("Your Notes:")
        for title, content in notes.items():
            print(f"Title: {title}")
            print(f"Content: {content}")
            print("-" * 20)
    else:
        print("No notes found.")

def delete_note():
    title = input("Enter title of note to delete: ")
    if title in notes:
        del notes[title]
        print(f"Note '{title}' deleted successfully!")
    else:
        print(f"Note '{title}' not found.")

def main_menu():
    while True:
        print("\nNOTE-FY")
        print("1. Add a Note")
        print("2. View All Notes")
        print("3. Delete a Note")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_note()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            delete_note()
        elif choice == '4':
            print("Thank you for using the Note-Making App. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main_menu()
