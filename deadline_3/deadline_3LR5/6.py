class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def __str__(self):
        return f'"{self.title}" ({self.author}, {self.year})'

    def __repr__(self):
        print()
books = [
    Book("Преступление и наказание", "Фёдор Достоевский", 1866),
    Book("Мастер и Маргарита", "Михаил Булгаков", 1967),
    Book("Война и мир", "Лев Толстой", 1869),
    Book("Гарри Поттер и философский камень", "Джоан Роулинг", 1997)
]
print("Список книг:")
for book in books:
    print(f"  - {book}")
