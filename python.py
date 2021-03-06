from klasser import Library
import csv


def enter_option():
    try:
        userInput = (int(input("\nEnter number accordingly if you want to:\n1.Add a book.\n2.Add a cd\n3.Add a movie\n6.show all lists\n0.to end\n\n>>")))
        return userInput
    except Exception:
        print("Wrong input, try again...")


# HÄR STARTAR PROGRAMMET
print("Welcome you media archive!")
a_library = Library()

# Alla filer laddas in
file_types = ["book_library.csv", "cds_library.csv", "movies_library.csv"]

# Läser in böcker och cdn här
for j in range(len(file_types)-1):
    try:
        with open(file_types[j], "r") as input_file:
            file_reader = csv.reader(input_file)

            # hoppar över första raden som är header i csv filen.
            next(file_reader)

            for row in file_reader:
                x = [row[0], row[1], row[2], row[3], row[4]]
                if j == 0:
                    a_library.add_book(x)

                elif j == 1:
                    a_library.add_cds(x)

    except Exception:
        print(f"{file_types[j]} file not found.")

# Läser in movies datafilen här istället
try:
    with open(file_types[2], "r") as input_file:
        file_reader = csv.reader(input_file)

        next(file_reader)

        for row in file_reader:
            x = [row[0], row[1], row[2], row[3], row[4], row[5]]
            a_library.add_movie(x)
except Exception:
    print(f"{file_types[2]} file not found.")

# Användaren kommer alltid hit
option_made = True
while option_made:
    # Värdet (användarens val) som assignas till option_made, kommer från funktion högst upp i filen
    option_chosen = enter_option()

    if option_chosen == 1:
        a_library.this_function(1)

    elif option_chosen == 2:
        a_library.this_function(2)

    elif option_chosen == 3:
        a_library.this_function(3)

    elif option_chosen == 6:
        a_library.this_function(6)

    # När användaren väljer 0, sparas allting till respektive medielista och avslutar programmet
    elif option_chosen == 0:
        def i_vars_func(i):
            return vars(i)

        my_books_data = []
        for i in a_library.books_list:
            my_books_data.append(i_vars_func(i))

        my_cds_data = []
        for i in a_library.cds_list:
            my_cds_data.append(i_vars_func(i))

        my_movied_data = []
        for i in a_library.movies_list:
            my_movied_data.append(i_vars_func(i))

        with open("book_library.csv", "w", newline='') as book_file:
            # changes made here
            fieldnames = ["title", "author", "nr_of_pages", "item_price", "purchase_year"]
            thewriter = csv.DictWriter(book_file, fieldnames=fieldnames)
            thewriter.writeheader()

            for data in my_books_data:
                thewriter.writerow(data)

        with open("cds_library.csv", "w", newline='') as cds_file:
            fieldnames = ["title", "singer", "total_length", "antal_spar", "item_price"]
            thewriter = csv.DictWriter(cds_file, fieldnames=fieldnames)
            thewriter.writeheader()

            for data in my_cds_data:
                thewriter.writerow(data)

        with open("movies_library.csv", "w", newline='') as movies_file:
            fieldnames = ["title", "director", "total_length", "item_price", "purchase_year", "grade"]
            thewriter = csv.DictWriter(movies_file, fieldnames=fieldnames)
            thewriter.writeheader()

            for data in my_movied_data:
                thewriter.writerow(data)

        print("Ok. End program. Goodbye!")
        option_made = False

    else:
        print("option N/A")
