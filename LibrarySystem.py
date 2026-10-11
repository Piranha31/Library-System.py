class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True
        print(f"{self.title} by {self.author} has been successfully borrowed !!!")

    def return_book(self):
        self.is_borrowed = False
        print(f"'{self.title}' by {self.author} has been returned to the library.")

book1 = book("Python crash course", "eric matthes")
book2 = book("harry Potter", "J.K rowling")
book3 = book("Atomic Habits", "James Clear")

book1.borrow()
book1.return_book()

book2.borrow()

book3.borrow()