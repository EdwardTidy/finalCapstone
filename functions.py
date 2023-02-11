import sqlite3

# Set up database to use
db = sqlite3.connect('data/ebookstore_db')
cursor = db.cursor()

# Add a new book to database
def enter_book():

    # Collect user information about book
    new_id = int(input("Please enter the id of the new book: "))
    new_title = input("Please enter the title of the new book: ")
    new_author = input("Please enter the author of the new book: ")
    new_quantity = int(input("Please enter the number of units of the new book in stock: "))

    #Add new book to database and inform user
    cursor.execute(("INSERT INTO books(id, Title, Author, Quantity) VALUES(?,?,?,?)"), (new_id, new_title, new_author, new_quantity))
    db.commit()
    print("New book added to database")

# Update book in database
def update_book():

    # Defensive programming loop to make sure correct id is selected
    while True:
        loop_break = "n"

        # Collect user information and then search database
        while True:
            update_id = int(input("Please enter the id of the book to be updated "))
            try:
                cursor.execute("SELECT Title FROM books WHERE id = ?", (update_id,))

                # Present book title in readable format for user and check correct
                selected_book = cursor.fetchone()
                selected_title = ""
                for title in selected_book:
                    selected_title = title
                option = input(f"You have selected: {selected_title} to be updated. Is this correct? y/n ").lower()
                if option == "y":
                    break
                else:
                    continue


            # Catch errors and flag them for user
            except TypeError:
                print("Unrecognised id, please try again ")
            except ValueError:
                print("Unrecognsed id, please try again")

        # Update book based on user input
        while True:
            # Display information about book for user
            cursor.execute("SELECT * FROM books WHERE id = ?", (update_id,))
            book_info = cursor.fetchall()
            for book_list in book_info:
                for information in book_list:
                    print(information)
            update_option = input("Would you like to update: 1: The id of the book. 2: The title of the book. 3: The Author of the book. Or 4: The Quantity of the Book? If you would not like to update anything please enter 0 to Quit ")

            # Update id
            if update_option == "1":
                new_id = int(input("Please enter the id to change this to: "))
                cursor.execute("UPDATE books SET id =? WHERE id = ?", (new_id, update_id))
                db.commit()

            # Update title
            elif update_option == "2":
                new_title = (input("Please enter the title to change this to: "))
                cursor.execute("UPDATE books SET title =? WHERE id = ?", (new_title, update_id))
                db.commit()

            # Update author
            elif update_option == "3":
                new_author = (input("Please enter the author to change this to: "))
                cursor.execute("UPDATE books SET author =? WHERE id = ?", (new_author, update_id))
                db.commit()

            # Update quantity
            elif update_option == "4":
                new_quantity = (input("Please enter the quantity to change this to: "))
                cursor.execute("UPDATE books SET quantity =? WHERE id = ?", (new_quantity, update_id))
                db.commit()
            
            # Quit function
            elif update_option == "0":
                loop_break = "y"
                break
        if loop_break == "y":
            break
        
# Delete book from database
def delete_book():

    # Loop to make sure correct book is deleted:
    while True:
        option = ""
        # Get user choice of book to delete (with try and except clauses to make sure entered id exists in database)
        try:
            delete_id = int(input("Please enter the id of the book to be deleted "))
            cursor.execute("SELECT Title FROM books WHERE id = ?", (delete_id,))

            # Present title of book to make sure this is correct
            selected_book = cursor.fetchone()
            selected_title = ""
            for title in selected_book:
                selected_title = title
            option = input(f"{selected_title} will be deleted, is this correct? y/n ").lower()
        
        # Except clauses to catch errors
        except TypeError:
            print("Input id not recognised, please try again")
        except ValueError:
            print("id's must be numbers in the form 300x, please try again")

        # If incorrect book provided, get user choice again
        if option == "n":
            continue
        # If correct book is selected delete it
        elif option == "y":
            break
    
    # Carry out deletion
    cursor.execute(("DELETE FROM books WHERE id = ?"), (delete_id,))
    print(f"{selected_title} has been deleted")
    db.commit()

# Search database for a book
def search_books():
    
    #Get user choice of search
    search_input = input("To search for books by id, please enter I, or to search for books by title, please enter T: ").lower()
    while True:

        # Searching by id
        if search_input == "i":
            while True:

                # Try clause to make sure id exists and is input correctly, if id is correct, print information about book
                try:
                    search_id = int(input("Please enter the id of the book you are searching for: "))
                    cursor.execute("SELECT * FROM books WHERE id = ?", (search_id,))
                    selected_book = cursor.fetchone()
                    for book in selected_book:
                        print(book)
                    search_input = "q"
                    break
                except TypeError:
                    print("Unrecognised id, please try again")
                except ValueError:
                    print("Unrecognised id, please try again, bear in mind id's take the form 300x")

        elif search_input == "t":
            while True:

                # Try clause to make sure title exists and is input correctly, if title is correct, print information about book
                try:
                    search_title = input("Please enter the title of the book you are searching for: ")
                    cursor.execute("SELECT * FROM books where Title = ?", (search_title,))
                    selected_book = cursor.fetchone()
                    for book in selected_book:
                        print(book)
                    search_input = "q"
                    break
                except TypeError:
                    print("Unrecognised title, please try again (remember titles are CaSe SeNsItIvE ")
                except ValueError:
                    print("Unrecognised title, please try again")

        # Else clause to flag unrecognised input
        else:
            search_input = input("Unrecognised command, please enter I to search by book id, T to search by book Title or Q to exit search: ").lower()
        if search_input == "q":
            break

