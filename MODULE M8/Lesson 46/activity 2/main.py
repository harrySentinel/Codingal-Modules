class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show_book(self):
        print("Book:", self.title)
        print("Author:", self.author)

book1 = Book("Python Basics", "Aditya Srivastava")
book2 = Book("Computer Notes", "Rohan Sharma")

book1.show_book()
print()
book2.show_book()
