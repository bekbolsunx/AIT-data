#     #27.11.2023 Exam pl
# class Person:
#     def _init_(self, id, name):
#         self.id = id
#         self.name = name


# class Book:
#     def _init_(self, id, name, author):
#         self.id = id
#         self.name = name
#         self.author = author


# class Library:   
#     def _init_(self, name):
#         self.name = name
#         self.books = {}
#         self.taken_books = {}

#     def add_books(self, book, amount=1):
#         self.books[book.id] = {
#             "Name": book.name,
#             "Author": book.author,
#             "Amount": amount,
#         }

#     def add_books_to_user(self, book, user):
#         if book.id in self.books and self.books[book.id]["Amount"] >= 1:
#             if user.id not in self.taken_books:
#                 self.taken_books[user.id] = [book.name]
#                 self.books[book.id]["Amount"] -= 1
#             else:
#                 self.taken_books[user.id].append(book.name)
#                 self.books[book.id]["Amount"] -= 1

#         else:
#             print("We have not this book")

#     def is_book_avlbl(self, book):
#         if self.books[book.id]["Amount"] >= 1:
#             print("Yes, we have this book")
#         else:
#             print("Sorry, we have not this book")

#     def how_many_books_takes(self, user):
#         return len(self.taken_books[user.id])


# akbar = Person(123, "Akbar")
# book = Book(122, "Ak-Keme", "Ch.Aitmatov")
# book2 = Book(1234, "Jamilya", "Ch.Aitmatov")
# state_lib = Library("Bishkek State Library")
# state_lib.add_books(book)
# state_lib.add_books(book2)
# state_lib.add_books_to_user(book, akbar)
# state_lib.add_books_to_user(book2, akbar)
# print(state_lib.how_many_books_takes(akbar))
# state_lib.is_book_avlbl(book)


# class Person:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name


# class Book:
#     def __init__(self, id, name, author):
#         self.id = id
#         self.name = name
#         self.author = author


# class Library:
#     def __init__(self, name):
#         self.name = name
#         self.books = {}
#         self.taken_books = {}

#     def add_books(self, book, amount=1):
#         self.books[book.id] = {
#             "Name": book.name,
#             "Author": book.author,
#             "Amount": amount,
#         }
  
#     def add_books_to_user(self, book, user):
#         if book.id in self.books and self.books[book.id]["Amount"] >= 1:
#             if user.id not in self.taken_books:
#                 self.taken_books[user.id] = [book.name]
#                 self.books[book.id]["Amount"] -= 1
#             else:
#                 self.taken_books[user.id].append(book.name)
#                 self.books[book.id]["Amount"] -= 1

#         else:
#             print("We have not this book")

#     def is_book_avlbl(self, book):
#         if self.books[book.id]["Amount"] >= 1:
#             print("Yes, we have this book")
#         else:
#             print("Sorry, we have not this book")

#     def how_many_books_takes(self, user):
#         return len(self.taken_books[user.id])


# akbar = Person(123, "Akbar")
# book = Book(122, "Ak-Keme", "Ch.Aitmatov")
# book2 = Book(1234, "Jamilya", "Ch.Aitmatov")
# state_lib = Library("Bishkek State Library")
# state_lib.add_books(book)
# state_lib.add_books(book2)
# state_lib.add_books_to_user(book, akbar)
# state_lib.add_books_to_user(book2, akbar)
# print(state_lib.how_many_books_takes(akbar))
# state_lib.is_book_avlbl(book)




################################################################################################################################################


