class Library:
    def __init__(self,book_name,author,available=True):
        self.book_name = book_name
        self.author = author
        self.available = available
        
    def check_out(self):
        if self.available:
           self.available = False
           print(f'"{self.book_name}"has been check out.')
        else:
           print(f'"{self.book_name}"is not available.')
           
    def return_book(self):
        self.available = True
        print(f'"{self.book_name}"has been returned.')
        
    def display_book(self):
        status = "Available"if self.available else "Not available"
        print(f"book:{self.book_name}, Author:{self.book_name},status:{self.book_name}")
        
book1 = Library("Python Programing","Gudio van Rossum")
book2 = Library("Data Structure","Mark Allen weiss")

book1.display_book()
book1.check_out()
book1.display_book()

book1.return_book()
book1.display_book()