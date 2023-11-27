from lib.book import Book

"""Test that Book object is initialised correctly and
attributes are set"""
def test_book_init():
    book = Book(1, 'test title', 'test author')
    assert book.id == 1
    assert book.title == 'test title'
    assert book.author_name == 'test author'


"""Test the equal behaviour - two different instances of a
Book with the same values should be equal"""
def test_equal():
    book1 = Book(1, 'test title', 'test author')
    book2 = Book(1, 'test title', 'test author')
    assert book1 == book2


"""Test the str method to see that the Book objects will be 
printed correctly"""
def test_repr_method():
    book1 = Book(1, 'test title', 'test author')
    assert str(book1) == 'Book(1, test title, test author)'

