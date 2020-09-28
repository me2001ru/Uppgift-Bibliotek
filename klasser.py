from funktioner import get_book_value, movie_start_worth
from klasser_2 import Book, Cd, Movie


class Library:

    def __init__(self):
        self.books_list = []
        self.cds_list = []
        self.movies_list = []
        self.media_lists = [self.books_list, self.cds_list, self.movies_list]

    def add_book(self, book):
        self.books_list.append(Book(*book))

    def add_cds(self, cd):
        self.cds_list.append(Cd(*cd))

    def add_movie(self, movie):
        self.movies_list.append(Movie(*movie))

    def print_list(self):
        # sort media_list before print executes

        # FIXME: sort-metoden har ingen inverkan !!!...
        # sorted(self.books_list, key=lambda book: book.title)
        # sorted(self.cds_list, key=lambda cd: cd.title)
        # sorted(self.movies_list, key=lambda cd: cd.title)

        for type_med in self.media_lists:
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

                # call function to set value on all same cds
                self.same_cd_set_value(title, singer, new_value)
            except Exception as e:
                print(e)

    def clean_string_list(self):
        argument = input("\n>>").split(",")
        new_argument = [i.strip() for i in argument]
        return new_argument

    def this_function(self, media_option):

        if media_option == 1:
            print("title, author, nr_of_pages, item_price, purchase_year")
            user_input = self.clean_string_list()
            book_worth = get_book_value(int(user_input[4]), int(user_input[3]))
            x = [user_input[0], user_input[1], user_input[2], book_worth, user_input[4]]
            self.add_book(x)

        elif media_option == 2:
            print("title, singer, total_length, antal_spar, item_price")
            user_input = self.clean_string_list()
            x = [user_input[0], user_input[1], user_input[2], user_input[3], user_input[4]]
            self.add_cds(x)

            # sätter värdet för alla cd-skivor
            self.cd_value(user_input[0], user_input[1], user_input[4])

        elif media_option == 6:
            self.print_list()

        else:
            print("title, director, total_length, item_price, purchase_year, slitage_gradering")
            user_input = self.clean_string_list()
            movie_worth = movie_start_worth(int(user_input[3]), int(user_input[4]), int(user_input[5]))
            x = [user_input[0], user_input[1], user_input[2], movie_worth, user_input[4], user_input[5]]
            self.add_movie(x)
