#tests.py
# Import all functions from the operations module
# This allows the test script to access all library management operations such as
# adding, updating, deleting books and members, as well as borrowing and returning books.
from operations import *

#TEST CASES

#Add Books
# Add first book with unique ISBN and valid details
assert add_book("SL001", "Intro to Programming", "Kairan Lebbie", "Non-Fiction", 5) == True

# Add second book ensuring proper author and genre
assert add_book("SL002", "Data Structures", "Haja Barrie", "Non-Fiction", 4) == True

# Add third book with correct total copies
assert add_book("SL003", "Operating Systems", "Julius Kargbo", "Non-Fiction", 3) == True

# Add fourth book verifying multiple entries by different authors
assert add_book("SL004", "Discrete Mathematics", "Ibrahim Swarray", "Non-Fiction", 2) == True

# Add fifth book confirming system handles multiple entries
assert add_book("SL005", "Database Systems", "Kumba Sesay", "Non-Fiction", 6) == True

# Add Books - Invalid Cases
# Fail: Duplicate ISBN should be rejected
assert add_book("SL001", "Advanced Programming", "Mohamed Kamara", "Non-Fiction", 2) == False

# Fail: Genre not in predefined list
assert add_book("SL006", "Quantum Physics", "Fatmata Conteh", "Article", 2) == False

# Fail: Negative total copies not allowed
assert add_book("SL007", "Impossible Book", "Alimamy Bangura", "Fiction", -1) == False

# Fail: Non-string ISBN should be rejected
assert add_book(123, "Numeric ISBN Book", "Alpha Sesay", "Fiction", 2) == False

# Add Members - Valid Cases
# Add first member with unique ID and valid email
assert add_member("905000001", "Sorie Kamara", "sorie.kamara@gmail.com") == True

# Add second member verifying correct email format
assert add_member("905000002", "Fatmata Kargbo", "fatmatakargbo@gmail.com") == True

# Add third member confirming system accepts multiple members
assert add_member("905000003", "Mohamed Conteh", "mohamed.conteh@gmail.com") == True

# Add Members - Invalid Cases
# Fail: Duplicate member ID should be rejected
assert add_member("905000001", "Bintu Sesay", "bintusesay@gmail.com") == False

# Fail: Invalid email format should be rejected
assert add_member("905000004", "Alpha Kamara", "alphakamara.com") == False

# Fail: Empty member name not allowed
assert add_member("905000005", "", "musasawyer@gmail.com") == False

# Fail: Non-string name should be rejected
assert add_member("905000006", 12345, "mohamedkamara@gmail.com") == False

# Update Book Details
# Update book title for SL001 successfully
assert update_book("SL001", title="Intro to Python") == True

# Update book author for SL001 successfully
assert update_book("SL001", author="Julius Kargbo") == True

# Update genre for SL002 to valid genre
assert update_book("SL002", genre="Fiction") == True

# Increase total copies of SL003 successfully
assert update_book("SL003", total_copies=5) == True

# Update Book - Invalid Cases
# Fail: Genre not in allowed list
assert update_book("SL002", genre="ScienceFiction") == False

# Borrow one copy to test borrowed count
borrow_book("SL003", "905000001")

# Fail: Cannot reduce total copies below borrowed copies
assert update_book("SL003", total_copies=0) == False

# Fail: Book ID does not exist
assert update_book("SL008", title="Linear Algebra") == False

# Update Member Details
# Update member name for 905000001 successfully
assert update_member("905000001", name="Sorie Kamara") == True

# Update email for 905000002 successfully
assert update_member("905000002", email="fatmatakargbo232@gmail.com") == True

# Update Member - Invalid Cases
# Fail: Member ID does not exist
assert update_member("905000999", name="Bintu Sesay") == False

# Fail: Invalid email format
assert update_member("905000003", email="fatmatakargbo.com") == False

# Fail: Empty member name not allowed
assert update_member("905000003", name="") == False

# Search Books
# Search by title returns True if found
assert search_books("Python") == True

# Search by author returns True if found
assert search_books("Haja Barrie", by="author") == True


#Search for non-existent title returns False
assert search_books("Emotional Intelligence", by="title") == False

#Search for non-existent author returns False
assert search_books("Mohamed Kamara", by="author") == False

# Delete Book Cases
# Delete book SL005 successfully
assert delete_book("SL005") == True

# Fail: Book ID does not exist
assert delete_book("SL010") == False

# Borrow book to test deletion constraint
borrow_book("SL001", "905000001")

# Fail: Cannot delete book that is currently borrowed
assert delete_book("SL001") == False

# Delete Member
# Delete member 905000003 successfully
assert delete_member("905000003") == True

# Fail: Member ID does not exist
assert delete_member("905099999") == False

# Borrow book to test deletion constraint
borrow_book("SL002", "905000002")

# Fail: Cannot delete member with borrowed books
assert delete_member("905000002") == False

# Borrow Book
# Member 905000002 borrows SL001 successfully
assert borrow_book("SL001", "905000002") == True

# Member 905000001 borrows SL002 successfully
assert borrow_book("SL002", "905000001") == True

# Member 905000002 borrows SL003 successfully
assert borrow_book("SL003", "905000002") == True

# Fail: Member cannot borrow the same book twice
assert borrow_book("SL001", "905000002") == False

# Fail: Book ID does not exist
assert borrow_book("SL010", "905000001") == False

# Fail: Member ID does not exist
assert borrow_book("SL001", "905099999") == False

# Borrow another book
borrow_book("SL004", "905000002")

# Borrow another book reaching limit
borrow_book("SL005", "905000002")

# Fail: Member has reached 3-book borrow limit
assert borrow_book("SL003", "905000002") == False

# Return Book
# Member returns a borrowed book successfully
assert return_book("SL002", "905000001") == True

# Fail: Book not borrowed by this member
assert return_book("SL004", "905000001") == False

# Fail: Book does not exist
assert return_book("SL010", "905000001") == False

# Fail: Member does not exist
assert return_book("SL001", "905099999") == False

print("All unit tests passed successfully!")
