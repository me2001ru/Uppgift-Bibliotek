
class Book:
    def __init__(self, title, author, nr_of_pages, item_price, purchase_year):

        self.title = title
        self.author = author
        self.nr_of_pages = nr_of_pages
        self.item_price = item_price
        self.purchase_year = purchase_year

    def __repr__(self):
        string = self.title + "\t" + self.author + "\t" + str(self.nr_of_pages) + "\t" + str(self.item_price) + "\t" + str(self.purchase_year)
        return string


class Cd:
    def __init__(self, title, singer, total_length, antal_spar, item_price):
        self.title = title
        self.singer = singer
        self.total_length = total_length
        self.antal_spar = antal_spar
        self.item_price = item_price

    def __repr__(self):
        string = self.title + "\t" + self.singer + "\t" + str(self.total_length) + "\t" + str(self.antal_spar) + "\t" + str(self.item_price)
        return string


class Movie:
    def __init__(self, title, director, total_length, item_price, purchase_year, grade):
        self.title = title
        self.director = director
        self.total_length = total_length
        self.item_price = item_price
        self.purchase_year = purchase_year
        self.grade = grade

    def __repr__(self):
        string = self.title + "\t" + self.director + "\t" + str(self.total_length) + "\t" + str(self.item_price) + "\t" + str(self.purchase_year)
        return string
