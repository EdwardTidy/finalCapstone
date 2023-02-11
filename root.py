import sqlite3
from functions import enter_book, update_book, delete_book, search_books

db = sqlite3.connect('data/ebookstore_db')
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Quantity INTEGER )
""")
db.commit()

books_list =[(3001, "A Tale of Two Cities", "Charles Dickens", 30),
            (3002, "Harry Potter and the Philosopher's Stone", "J. K. Rowling", 40), 
            (3003, "The Lion, The Witch and the Wardrobe", "C.S. Lewis", 25), 
            (3004, "The Lord of the Rings", "J.R.R Tolkien", 37), 
            (3005, "Alice in Wonderland", "Lewis Carroll", 12)]

#Using REPLACE INTO as in this case we may run the code multiple times, in which case INSERT INTO throws an error as we are trying to overrwrite existing unique values. IRL I don't know whether this would usually be part of the process of running a database so have used REPLACE as a workaround in the meantime
cursor.executemany("""
REPLACE INTO books(id, Title, Author, Quantity) VALUES(?,?,?,?)
""", books_list)
db.commit()

#Code for functions in functions.py file
while True:
    # Get user input for function to execute
    user_input = input("Menu: 1: Enter book. 2: Update book. 3: Delete book. 4: Search books. 0: Exit ")
    while True:
        if user_input == "1":
            enter_book()
        elif user_input == "2":
            update_book()
        elif user_input == "3":
            delete_book()
        elif user_input == "4":
            search_books()
        elif user_input == "0":
            print("Quitting")
            break
        # Catch any errors in input
        else:
            while True:
                user_input = input("Unrecognised command. Please enter 1 (Enter Book), 2 (Update book), 3 (Delete book), 4 (Search books) or 0 (Quit program) ")
                if user_input == "1" or user_input == "2" or user_input == "3" or user_input == "4" or user_input == "0":
                    break
        user_input = input("Menu: 1: Enter book. 2: Update book. 3: Delete book. 4: Search books. 0: Exit ")
    if user_input == "0":
        break

db.commit()

db.close()