class Library():
    def __init__(self):
        self.books = []

    def show_books(self):
        if(len(self.books) > 0):
            print('Available Books:')
            for book in self.books:
                print(book)
        else:
            print('Library is empty. Add books')
        
    def add_book(self, book):    
        self.books.append(book)

    def remove_book(self, book):    
        if book in self.books:
            self.books.remove(book)
            print(f"{book} removed from library")
        else:
            print("Book not found") 

lib = Library()
lib.show_books()
lib.add_book("Python Basics")
lib.add_book("Clean Code")
lib.remove_book("Clean Code")
lib.show_books()

