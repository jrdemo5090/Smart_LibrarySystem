SmartLibrary System
===================

Overview
--------
SmartLibrary is a simple library management system that allows you to:
- Add, read, update, and delete books (CRUD operations)
- Borrow and return books
- Run tests to verify that the system works correctly

Requirements
------------
- Python 3.12 or higher installed
- All project files must be in the same folder

Files
-----
Place the following files inside a folder named SmartLibrary. For example: C:\Users\YourName\Documents\SmartLibrary
- operations.py : Contains all functions for CRUD and borrow/return operations
- demo.py       : Main script to run the library system
- tests.py      : Contains test cases to verify functionality
- README.md     : This instruction file

How to Run
----------
1. Open Command Prompt on Windows by pressing Windows + R, typing cmd, and pressing Enter.
2. Navigate to the project folder by typing: 
   cd C:\Users\YourName\Documents\SmartLibrary
3. To run the main program, type:
   python demo.py
   - Follow the on-screen instructions to add, view, borrow, return, or delete books.
4. To run the tests and verify functionality, type:
   python tests.py
   - This will automatically check all functions in operations.py to ensure they work correctly.

Notes
-----
- Ensure that operations.py, demo.py, and tests.py are all in the same SmartLibrary folder.
- All data is stored in memory; closing the program will erase current records.
- Running the tests before using the main program is recommended to confirm everything is functioning properly.
