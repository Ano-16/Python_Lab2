class LibraryManager:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author, publisher, volume, year, isbn):
        """Add a book to the library."""
        if isbn in self.books:
            print(f"Book with ISBN {isbn} already exists.")
            return
        self.books[isbn] = {
            'title': title,
            'author': author,
            'publisher': publisher,
            'volume': volume,
            'year': year,
            'isbn': isbn
        }
        print(f"Book '{title}' added to the library.")

    def remove_book(self, isbn):
        """Remove a book from the library by its ISBN."""
        if isbn in self.books:
            del self.books[isbn]
            print(f"Book with ISBN {isbn} removed from the library.")
        else:
            print(f"No book found with ISBN {isbn}.")

    def get_book_details(self, isbn):
        """Retrieve and display the details of a book using its ISBN."""
        if isbn in self.books:
            return self.books[isbn]
        else:
            print(f"No book found with ISBN {isbn}.")
            return None

    def search_books(self, search_term, search_type='title'):
        """Search for books by title or author."""
        results = []
        for book in self.books.values():
            if search_type == 'title' and search_term.lower() in book['title'].lower():
                results.append(book)
            elif search_type == 'author' and search_term.lower() in book['author'].lower():
                results.append(book)
        return results

    def list_books(self):
        """List all books currently in the library."""
        return list(self.books.values())

    def update_book(self, isbn, **kwargs):
        """Update the details of an existing book."""
        if isbn in self.books:
            self.books[isbn].update(kwargs)
            print(f"Book with ISBN {isbn} updated.")
        else:
            print(f"No book found with ISBN {isbn}.")

    def is_book_available(self, isbn):
        """Check if a book is available in the library by its ISBN."""
        return isbn in self.books

# Example usage of the LibraryManager
if __name__ == "__main__":
    
    library = LibraryManager()

    # Adding sample books
    library.add_book("Operating Systems: Three Easy Pieces", "Remzi H. Arpaci-Dusseau", "Arpaci-Dusseau Books", 1, 2020, "1234567890123")
    library.add_book("Data Structures and Algorithm Analysis in C++", "Mark Allen Weiss", "Pearson", 4, 2021, "1234567890124")
    library.add_book("Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow", "Aurélien Géron", "O'Reilly Media", 2, 2023, "1234567890125")

    # Removing a book
    library.remove_book("1234567890124")

    # Retrieving the details of a book
    book_details = library.get_book_details("1234567890123")
    if book_details:
        print("Book details:", book_details)

    # Searching for books by title
    search_results = library.search_books("Machine Learning")
    print("Search results by title:", search_results)

    # Searching for books by author
    search_results = library.search_books("Aurélien Géron", search_type='author')
    print("Search results by author:", search_results)

    # Listing all books
    all_books = library.list_books()
    print("All books in the library:", all_books)

    # Updating book details
    library.update_book("1234567890125", title="Hands-On Machine Learning with Scikit-Learn and TensorFlow", volume=3)

    # Checking the availability of a book
    is_available = library.is_book_available("1234567890125")
    print("Is the book available?", is_available)
