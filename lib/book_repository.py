from lib.book import Book

class BookRepository:
    def __init__(self, connection):
        # Set up object with connection to db
        self._connection = connection

    def all(self):
        # Returns a list of Book objects for all the books in the db
        rows = self._connection.execute('SELECT * FROM books')
        books = []
        for row in rows:
            book = Book(row['id'], row['title'], row['author_name'])
            books.append(book)
        return books