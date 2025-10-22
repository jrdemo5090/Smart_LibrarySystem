from operations import *
import ast

# Simple display functions
def display_books():
    """Shows all the books in the library in a readable way."""
    if not books:
        print("\nNo books in the library.")
        return
    print("\n--- Books in Library ---")
    for isbn, book in books.items():
        print(f"ISBN: {isbn}: {book}")


def display_members():
    """Shows all the library members in a readable way."""
    if not members:
        print("\nNo members in the library.")
        return
    print("\n--- Library Members ---")
    for member in members:
        print(member)


def parse_input(prompt, expected_type=None):
    """
    This function asks the user for input and tries to convert it into the right type.

    - prompt: the message shown to the user
    - expected_type: if given, checks that the input is the right type (like str or int)

    If the user makes a mistake, it tells them what kind of input is expected.
    Works for numbers, text, or other simple values.
    """
    while True:
        user_input = input(prompt).strip()
        try:
            value = ast.literal_eval(user_input)
        except (ValueError, SyntaxError):
            print("Invalid input format. For strings, enclose in quotes (e.g., 'Python'). For numbers, enter without "
                  "quotes.")
            continue

        if expected_type and not isinstance(value, expected_type):
            type_name = (
                "string" if expected_type == str else "integer" if expected_type == int else expected_type.__name__
            )
            print(f"Oops! This field needs a {type_name}. Try again.")
            continue

        return value


def main_menu():
    """The main menu that shows all options and handles user choices."""
    while True:
        print("\n--- Welcome to the Smart Library System ---")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Search Books")
        print("4. Update Book")
        print("5. Update Member")
        print("6. Delete Book")
        print("7. Delete Member")
        print("8. Borrow Book")
        print("9. Return Book")
        print("0. Exit")

        choice = input("Select an option (0-9): ").strip()

        if choice == "1":
            print("\n--- Add Book ---")
            print(f"Guideline: Enter values one by one. Strings must be in quotes. Genre must be a valid string "
                  f"from {genres}. Total Copies must be an integer without quotes.")
            isbn = parse_input("Enter ISBN (string, e.g., 'SL001'): ", expected_type=str)
            title = parse_input("Enter Title (string, e.g., 'Intro to Python'): ", expected_type=str)
            author = parse_input("Enter Author (string, e.g., 'Julius Kargbo'): ", expected_type=str)
            genre = parse_input(f"Enter Genre {genres} (string, e.g., 'Fiction'): ", expected_type=str)
            total_copies = parse_input("Enter Total Copies (integer, e.g., 5): ", expected_type=int)

            if add_book(isbn, title, author, genre, total_copies):
                print("Book added successfully!")
            else:
                print("Failed to add book. Check inputs, genre validity, or duplicate ISBN.")

            display_books()
            display_members()

        elif choice == "2":
            print("\n--- Add Member ---")
            print("Guideline: Strings must be in quotes. Email must contain '@' and '.'")
            member_id = parse_input("Enter Member ID (string, e.g., 'M001'): ", expected_type=str)
            name = parse_input("Enter Name (string, e.g., 'John Doe'): ", expected_type=str)
            email = parse_input("Enter Email (string, e.g., 'john@example.com'): ", expected_type=str)

            if add_member(member_id, name, email):
                print("Member added successfully!")
            else:
                print("Failed to add member. Check inputs, email format, or duplicate Member ID.")

            display_books()
            display_members()

        elif choice == "3":
            print("\n--- Search Books ---")
            print("Guideline: Strings must be in quotes. You can search by 'title' or 'author'.")
            query = parse_input("Enter search query (string, e.g., 'Python'): ", expected_type=str)
            by = parse_input("Search by ('title' or 'author', default='title'): ", expected_type=str)
            if by not in ["title", "author"]:
                by = "title"

            found = search_books(query, by)
            print("Book(s) found!" if found else "No books matched your search.")

            display_books()
            display_members()

        elif choice == "4":
            print("\n--- Update Book ---")
            print(f"Guideline: Enter ISBN first. Optional updates: strings in quotes, genre must be valid, "
                  f"total copies as integer without quotes. Leave blank to skip.")
            isbn = parse_input("Enter ISBN of book to update (string, e.g., 'SL001'): ", expected_type=str)
            title_input = input("New Title (string, leave blank to skip): ").strip()
            title = ast.literal_eval(title_input) if title_input else None
            author_input = input("New Author (string, leave blank to skip): ").strip()
            author = ast.literal_eval(author_input) if author_input else None
            genre_input = input(f"New Genre {genres} (leave blank to skip): ").strip()
            genre = ast.literal_eval(genre_input) if genre_input else None
            total_copies_input = input("New Total Copies (integer, leave blank to skip): ").strip()
            total_copies = int(total_copies_input) if total_copies_input else None

            if update_book(isbn, title, author, genre, total_copies):
                print("Book updated successfully!")
            else:
                print("Failed to update book. Check ISBN, genre validity, or inputs.")

            display_books()
            display_members()

        elif choice == "5":
            print("\n--- Update Member ---")
            print("Guideline: Enter Member ID first. Optional updates: strings in quotes, "
                  "email must contain '@' and '.'")
            member_id = parse_input("Enter Member ID to update (string, e.g., 'M001'): ", expected_type=str)
            name_input = input("New Name (string, leave blank to skip): ").strip()
            name = ast.literal_eval(name_input) if name_input else None
            email_input = input("New Email (string, leave blank to skip): ").strip()
            email = ast.literal_eval(email_input) if email_input else None

            if update_member(member_id, name, email):
                print("Member updated successfully!")
            else:
                print("Failed to update member. Check Member ID or email format.")

            display_books()
            display_members()

        elif choice == "6":
            print("\n--- Delete Book ---")
            print("Guideline: Enter ISBN as string in quotes. Cannot delete book if copies are borrowed.")
            isbn = parse_input("Enter ISBN of book to delete (string, e.g., 'SL001'): ", expected_type=str)

            if delete_book(isbn):
                print("Book deleted successfully!")
            else:
                print("Failed to delete book. It may have borrowed copies or invalid ISBN.")

            display_books()
            display_members()

        elif choice == "7":
            print("\n--- Delete Member ---")
            print("Guideline: Enter Member ID as string in quotes. Cannot delete member if they have borrowed books.")
            member_id = parse_input("Enter Member ID to delete (string, e.g., 'M001'): ", expected_type=str)

            if delete_member(member_id):
                print("Member deleted successfully!")
            else:
                print("Failed to delete member. They may have borrowed books or invalid ID.")

            display_books()
            display_members()

        elif choice == "8":
            print("\n--- Borrow Book ---")
            print("Guideline: Enter ISBN and Member ID as strings in quotes. Max 3 books per member. "
                  "Cannot borrow the same book twice.")
            isbn = parse_input("Enter ISBN to borrow (string, e.g., 'SL001'): ", expected_type=str)
            member_id = parse_input("Enter Member ID (string, e.g., 'M001'): ", expected_type=str)

            if borrow_book(isbn, member_id):
                print("Book borrowed successfully!")
            else:
                print("Failed to borrow book. Check availability, member ID, or borrowing limits.")

            display_books()
            display_members()

        elif choice == "9":
            print("\n--- Return Book ---")
            print("Guideline: Enter ISBN and Member ID as strings in quotes. Book must be borrowed by the member.")
            isbn = parse_input("Enter ISBN to return (string, e.g., 'SL001'): ", expected_type=str)
            member_id = parse_input("Enter Member ID (string, e.g., 'M001'): ", expected_type=str)

            if return_book(isbn, member_id):
                print("Book returned successfully!")
            else:
                print("Failed to return book. Check if the member borrowed it.")

            display_books()
            display_members()

        elif choice == "0":
            print("Exiting the library system. Goodbye!")
            break

        else:
            print("Invalid option. Please select a number between 0 and 9.")


if __name__ == "__main__":
    main_menu()
