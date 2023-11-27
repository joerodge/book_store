class Book:
    def __init__(self, id, title, author_name):
        # Create book object with attributes in db
        self.id = id
        self.title = title
        self.author_name = author_name

    def __eq__(self, other):
        # Make it so book objects with same values are equal
        return self.__dict__ == other.__dict__

    def __repr__(self):
        # Define the str() and print behaviour so we can see the output
        return f"Book({self.id}, {self.title}, {self.author_name})"

