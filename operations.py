# Global data structures
books = {}  # Stores books using ISBN as the key
members = []  # List of dictionaries representing library members
genres = ("Fiction", "Non-Fiction", "Sci-Fi", "Mystery", "Biography")  # Predefined book categories

# Add Book
def add_book(isbn, title, author, genre, total_copies):
    """
    Registers a new book in the library inventory.
    Ensures the ISBN is unique, the genre is recognized, and the total copies are valid.
    Returns True if the book is successfully added, otherwise returns False.
    """
    if not isinstance(isbn, str):
        return False
    if not isinstance(title, str):
        return False
    if not isinstance(author, str):
        return False
    if not isinstance(genre, str):
        return False
    if not isinstance(total_copies, int) or total_copies < 0:
        return False
    if genre not in genres:
        return False
    if isbn in books:
        return False

    books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "total_copies": total_copies,
        "original_copies": total_copies
    }
    return True

# Add Member
def add_member(member_id, name, email):
    """
    Enrolls a new member into the library system.
    Validates uniqueness of member ID and proper email formatting.
    Returns True upon successful addition, otherwise False.
    """
    if not isinstance(member_id, str):
        return False
    if not isinstance(name, str) or len(name.strip()) == 0:
        return False
    if not isinstance(email, str) or "@" not in email or "." not in email:
        return False
    for member in members:
        if member["member_id"] == member_id:
            return False

    members.append({
        "member_id": member_id,
        "name": name,
        "email": email,
        "borrowed_books": []
    })
    return True

# Search Books
def search_books(query, by="title"):
    """
    Performs a case-insensitive search for books by title or author.
    Returns True if at least one matching book is found, otherwise returns False.
    """
    if not isinstance(query, str):
        return False
    if not isinstance(by, str):
        return False

    for isbn, book in books.items():
        if by.lower() == "author":
            if query.lower() in book["author"].lower():
                return True
        else:
            if query.lower() in book["title"].lower():
                return True
    return False

# Update Book
def update_book(isbn, title=None, author=None, genre=None, total_copies=None):
    """
    Modifies details of an existing book in the library.
    Accepts optional updates for title, author, genre, and total copies.
    Returns True immediately after updating a valid field, otherwise False.
    """
    if not isinstance(isbn, str) or isbn not in books:
        return False

    book = books[isbn]

    if title is not None:
        if not isinstance(title, str):
            return False
        book["title"] = title
        return True

    if author is not None:
        if not isinstance(author, str):
            return False
        book["author"] = author
        return True

    if genre is not None:
        if not isinstance(genre, str) or genre not in genres:
            return False
        book["genre"] = genre
        return True

    if total_copies is not None:
        if not isinstance(total_copies, int) or total_copies < 0:
            return False
        borrowed_count = book["original_copies"] - book["total_copies"]
        if total_copies < borrowed_count:
            return False
        book["total_copies"] = total_copies
        book["original_copies"] = max(book.get("original_copies", total_copies), total_copies)
        return True

    return False

# Update Member
def update_member(member_id, name=None, email=None):
    """
    Updates information of a library member.
    Allows modification of the member’s name and email.
    Returns True upon successful update, otherwise False.
    """
    if not isinstance(member_id, str):
        return False

    for member in members:
        if member["member_id"] == member_id:
            if name is not None:
                if not isinstance(name, str) or len(name.strip()) == 0:
                    return False
                member["name"] = name
                return True
            if email is not None:
                if not isinstance(email, str) or "@" not in email or "." not in email:
                    return False
                member["email"] = email
                return True
    return False

# Delete Book
def delete_book(isbn):
    """
    Removes a book from the library inventory if no copies are borrowed.
    Returns True if deletion succeeds, otherwise False.
    """
    if not isinstance(isbn, str) or isbn not in books:
        return False

    book = books[isbn]
    borrowed_count = book["original_copies"] - book["total_copies"]
    if borrowed_count > 0:
        return False

    del books[isbn]
    return True

# Delete Member
def delete_member(member_id):
    """
    Deletes a library member if they have no borrowed books.
    Returns True if deletion succeeds, otherwise False.
    """
    if not isinstance(member_id, str):
        return False

    for member in members:
        if member["member_id"] == member_id:
            if len(member["borrowed_books"]) > 0:
                return False
            members.remove(member)
            return True
    return False

# Borrow Book
def borrow_book(isbn, member_id):
    """
    Allows a member to borrow a book, adhering to availability and borrowing limits.
    Returns True if the book is successfully borrowed, otherwise False.
    """
    if not isinstance(isbn, str) or not isinstance(member_id, str):
        return False
    if isbn not in books:
        return False

    book = books[isbn]
    if book["total_copies"] <= 0:
        return False

    for member in members:
        if member["member_id"] == member_id:
            if not isinstance(member["borrowed_books"], list):
                return False
            if len(member["borrowed_books"]) >= 3:
                return False
            if isbn in member["borrowed_books"]:
                return False
            member["borrowed_books"].append(isbn)
            book["total_copies"] -= 1
            return True
    return False

# Return Book
def return_book(isbn, member_id):
    """
    Processes the return of a borrowed book by a member.
    Returns True if successful, otherwise False.
    """
    if not isinstance(isbn, str) or not isinstance(member_id, str):
        return False
    if isbn not in books:
        return False

    for member in members:
        if member["member_id"] == member_id:
            if not isinstance(member["borrowed_books"], list):
                return False
            if isbn not in member["borrowed_books"]:
                return False
            member["borrowed_books"].remove(isbn)
            books[isbn]["total_copies"] += 1
            return True
    return False
