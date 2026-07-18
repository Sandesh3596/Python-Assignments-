class BookStore:
    NoOfBooks = 0

    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoOfBooks += 1

    def Display(self):
        print(f"{self.Name} by {self.Author}. No of books: {BookStore.NoOfBooks}")


b1 = BookStore("Wings of Fire", "A.P.J. Abdul Kalam")
b2 = BookStore("The Alchemist", "Paulo Coelho")

b1.Display()
b2.Display()