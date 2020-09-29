
class Book:
    def __init__(self, title, author, nr_of_pages, item_price, purchase_year):

        self.title = title
        self.author = author
        self.nr_of_pages = nr_of_pages
        self.item_price = int(item_price)
        self.purchase_year = purchase_year

    def __repr__(self):
        string = "{:20s}{:20s}{:20s}{:20s}{:20s}".format(self.title, str(self.item_price), self.author, str(self.nr_of_pages), str(self.purchase_year))
        return string


class Cd:
    def __init__(self, title, singer, total_length, antal_spar, item_price):
        self.title = title
        self.singer = singer
        self.total_length = total_length
        self.antal_spar = antal_spar
        self.item_price = int(item_price)

    def __repr__(self):
        string = "{:20s}{:20s}{:20s}{:20s}{:20s}".format(self.title, str(self.item_price), self.singer, str(self.total_length), str(self.antal_spar))
        return string


class Movie:
    def __init__(self, title, director, total_length, item_price, purchase_year, grade):
        self.title = title
        self.director = director
        self.total_length = total_length
        self.item_price = int(item_price)
        self.purchase_year = purchase_year
        self.grade = grade

    def __repr__(self):
        string = "{:20s}{:20s}{:20s}{:20s}{:20s}".format(self.title, str(self.item_price), self.director, str(self.total_length), str(self.purchase_year))
        return string
