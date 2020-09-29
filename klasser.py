from funktioner import get_book_value, movie_start_worth
from klasser_2 import Book, Cd, Movie
import operator


class Library:

    def __init__(self):
        self.books_list = []
        self.cds_list = []
        self.movies_list = []
        self.media_lists = [self.books_list, self.cds_list, self.movies_list]

    # Först skapas funktionen med klassen Book, Cd eller Movie, för att sedan läggas in i sin lista
    def add_book(self, book):
        self.books_list.append(Book(*book))

    def add_cds(self, cd):
        self.cds_list.append(Cd(*cd))

    def add_movie(self, movie):
        self.movies_list.append(Movie(*movie))

    def print_list(self):

        choice_of_sort = int(input("Sort by title (1) or price (2): "))

        # Listor sorteras efter den attributen användaren väljer att sortera efter.
        if choice_of_sort == 1:
            self.books_list.sort(key=operator.attrgetter('title'))
            self.cds_list.sort(key=operator.attrgetter('title'))
            self.movies_list.sort(key=operator.attrgetter('title'))
        else:
            self.books_list.sort(key=operator.attrgetter('item_price'))
            self.cds_list.sort(key=operator.attrgetter('item_price'))
            self.movies_list.sort(key=operator.attrgetter('item_price'))

        # Här börjar utskriften
        print("{:20s}{:20s}{:20s}{:20s}{:20s}".format("Title", "Price", "Auth/Dir/Singer", "Length", "Year bought/# Of tracks"))
        print("----------------------------------------------------\n")

        for type_med in self.media_lists:
            print()
            for line in type_med:
                print(line)

    def same_cd_set_value(self, title, singer, new_value):
        for i in self.cds_list:
            if i.title == title and i.singer == singer:
                i.item_price = new_value

    def cd_value(self, title, singer, price):
        counter = 0
        if len(self.cds_list) > 0:
            for i in self.cds_list:
                if i.title == title and i.singer == singer:
                    counter += 1
        else:
            return price

        if counter > 0:
            try:
                new_value = (round(int(price) / counter))

                # kallar funktion för att get värdet på alla samma cdn
                self.same_cd_set_value(title, singer, new_value)
            except Exception as e:
                print(e)

    def clean_string_list(self):
        argument = input("\n>>").split(",")
        new_argument = [i.strip() for i in argument]
        return new_argument

    def this_function(self, media_option):

        if media_option == 1:
            print("Title, Author, Nr of pages, Item price, Purchase year")
            user_input = self.clean_string_list()
            book_worth = get_book_value(int(user_input[4]), int(user_input[3]))
            x = [user_input[0], user_input[1], user_input[2], book_worth, user_input[4]]
            self.add_book(x)

        elif media_option == 2:
            print("Title, Singer, Total length, Nr of tracks, Item price")
            user_input = self.clean_string_list()
            x = [user_input[0], user_input[1], user_input[2], user_input[3], user_input[4]]
            self.add_cds(x)

            # sätter värdet för alla cd-skivor
            self.cd_value(user_input[0], user_input[1], user_input[4])

        elif media_option == 6:
            self.print_list()

        else:
            print("Title, Director, Total length, Item price, Purchase year, Slitage gradering")
            user_input = self.clean_string_list()
            movie_worth = movie_start_worth(int(user_input[3]), int(user_input[4]), int(user_input[5]))
            x = [user_input[0], user_input[1], user_input[2], movie_worth, user_input[4], user_input[5]]
            self.add_movie(x)
