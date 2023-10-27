class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        all_royalties = 0
        royalties_list = [contract.royalties for contract in self.contracts()]
        for amount in royalties_list:
            all_royalties += amount
        return all_royalties


class Book:
    
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]


class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            raise Exception("The author must be an Author instance.")
    
    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, new_book):
        if isinstance(new_book, Book):
            self._book = new_book
        else:
            raise Exception("The book must be a Book instance.")

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, new_date):
        if type(new_date) is str:
            self._date = new_date
        else:
            raise Exception("The date must be a string.")

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, new_royalties):
        if type(new_royalties) is int:
            self._royalties = new_royalties
        else:
            raise Exception("The royalties must be a number.")

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
    